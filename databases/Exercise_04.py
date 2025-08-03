'''
Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:
    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query
BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!
'''

print("Application name: URBN Escalante Parking\n")
user_name = str(input(f"Insert your name: "))

from sqlalchemy import create_engine, func, text, select, ForeignKey, Boolean, MetaData,Table, Column, Integer, String, Enum, DateTime, MetaData

import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")
DB_NAME = os.getenv("MYSQL_DATABASE_EXERCISES")

# Build database URL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create the new database in MySQL Workbench
db_name = "parking_URBN_db"

with engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
    print(f"\nDatabase '{db_name}' created or already exists.")

metadata = MetaData()

# create at least 3 tables: 
users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("email", String(100), nullable=False, unique=True),
    Column("role", Enum("owner", "visitor"), nullable=True),
    Column("sinpe_number", String(15), nullable=True, unique=True),
    Column("created_at", DateTime, server_default=func.now())
)

parking_spaces = Table(
    "parking_spaces", metadata,
    Column("id", Integer, primary_key=True),
    Column("owner_id", Integer, ForeignKey("users.id")),
    Column("floor", Integer, nullable=False),
    Column("number", String(10), nullable=False),
    Column("is_available", Boolean, default=True),
    Column("price_per_hour", Integer, nullable=False)
)

rentals = Table(
    "rentals", metadata,
    Column("id", Integer, primary_key=True),
    Column("space_id", Integer, ForeignKey("parking_spaces.id")),
    Column("visitor_id", Integer, ForeignKey("users.id")),
    Column("start_time", DateTime, nullable=False),
    Column("end_time", DateTime, nullable=False),
    Column("total_price", Integer, nullable=False)
)

# insert data to each table (as a function to call it later):
def insert_users():
    print("\n🟢 Insert a New User")

    name = input("Full name: ").strip()
    email = input("Email: ").strip()
    role = input("Role (owner/visitor): ").strip().lower()

    sinpe_number = None
    if role == "owner":
        sinpe_number = input("SINPE number (format XXXXXXXX): ").strip()
        if len(sinpe_number) != 8:
            print("❌ Invalid SINPE number format.")
            return

    elif role != "visitor":
        print("❌ Invalid role. Must be 'owner' or 'visitor'.")
        return

    try:
        with engine.connect() as conn:
            insert_stmt = users.insert().values(
                name=name,
                email=email,
                role=role,
                sinpe_number=sinpe_number
            )
            conn.execute(insert_stmt)
            print("✅ User inserted successfully.")

    except Exception as e:
        print(f"❌ Error inserting user: {e}")

# check on sinpe
def is_valid_sinpe(sinpe):
    return sinpe.isdigit() and len(sinpe) == 8

# update data in each table (as a function to call it later): 
def update_users():
    print("\n🔄 Update User Data")
    email_to_update = input("Enter the email of the user to update: ").strip()
    with engine.connect() as conn:
        user_exists = conn.execute(select(users).where(users.c.email == email_to_update)).fetchone()
        if not user_exists:
            print("⚠️ User not found.")
            return
    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Email")
    print("3. Role")
    print("4. SINPE number")

    option = input("Choose an option (1-4): ").strip()

    update_column = None
    new_value = None

    if option == "1":
        update_column = users.c.name
        new_value = input("Enter the new name: ").strip()

        if not new_value:
            print("❌ Name cannot be empty.")
            return

    elif option == "2":
        new_value = input("Enter the new email: ").strip()
        # Check if the new email already exists (important, it is the PK)
        with engine.connect() as conn:
            check_stmt = select(users).where(users.c.email == new_value)
            existing_user = conn.execute(check_stmt).fetchone()
            if existing_user:
                print("❌ This email is already in use. Please choose a different one.")
                return
        update_column = users.c.email

    elif option == "3":
        new_value = input("Enter the new role (owner/visitor): ").strip().lower()
        if new_value not in ("owner", "visitor"):
            print("❌ Invalid role.")
            return
        update_column = users.c.role

        with engine.connect() as conn:

            if new_value == "owner":
                # Check if SINPE is filled already, if not, ask for it (all owners must have SINPE)
                check_sinpe = select(users.c.sinpe_number).where(users.c.email == email_to_update)
                result = conn.execute(check_sinpe).fetchone()

                if result is None:
                    print("⚠️ User not found.")
                    return
                
                if result.sinpe_number is None:
                    print("ℹ️ This user does not have a SINPE number yet.")
                    sinpe = input("Please enter SINPE number (XXXXXXXX): ").strip()
                    if not is_valid_sinpe(sinpe):
                        print("❌ Invalid SINPE format.")
                        return

                    # Update role and SINPE together
                    stmt = (
                        users.update()
                        .where(users.c.email == email_to_update)
                        .values({users.c.role: new_value, users.c.sinpe_number: sinpe})
                    )
                else:
                    # SINPE already exists, only update role
                    stmt = (
                        users.update()
                        .where(users.c.email == email_to_update)
                        .values({users.c.role: new_value})
                    )
            
            else:
                # If new role is visitor, remove SINPE
                stmt = (
                    users.update()
                    .where(users.c.email == email_to_update)
                    .values({users.c.role: new_value, users.c.sinpe_number: None})
                )

            updated = conn.execute(stmt)

            if updated.rowcount:
                if new_value == "visitor":
                    print("✅ Role updated and SINPE removed successfully.")
                elif new_value == "owner" and result.sinpe_number is None:
                    print("✅ Role and SINPE updated successfully.")
                else:
                    print("✅ Role updated successfully.")
                
            else:
                print("⚠️ No user found.")

            return

    elif option == "4":

        new_value = input("Enter the new SINPE number (XXXXXXXX): ").strip()
        if not is_valid_sinpe(new_value):
            print("❌ Invalid SINPE format.")
            return
        
        with engine.connect() as conn:
            result = conn.execute(select(users.c.role).where(users.c.email == email_to_update)).fetchone()
            if result is None:
                print("⚠️ User not found.")
                return
            if result.role != "owner":
                print("❌ Only users with role 'owner' can have a SINPE number.")
                return
        
        update_column = users.c.sinpe_number

    else:
        print("❌ Invalid option.")
        return

    try:
        with engine.connect() as conn:
            stmt = (
                users.update()
                .where(users.c.email == email_to_update)
                .values({update_column: new_value})
            )
            result = conn.execute(stmt)
            if result.rowcount:
                print("✅ User updated successfully.")
            else:
                print("⚠️ No user found with that email.")
    except Exception as e:
        print(f"❌ Error updating user: {e}")

def select_users():
    print("\n🔍 Select Users")
    print("1. List all users")
    print("2. Search user by email")
    option = input("Choose an option (1-2): ").strip()

    with engine.connect() as conn:
        if option == "1":
            # List all users
            stmt = select(users)
            result = conn.execute(stmt).fetchall()
            if result:
                for row in result:
                    if row.role == "owner":
                        print(f"Name: {row.name}, Email: {row.email}, Role: {row.role}, SINPE: {row.sinpe_number}")
                    else:
                        print(f"Name: {row.name}, Email: {row.email}, Role: {row.role}")
            else:
                print("⚠️ No users found.")

        elif option == "2":
            email_search = input("Enter email to search: ").strip()
            stmt = select(users).where(users.c.email == email_search)
            result = conn.execute(stmt).fetchone()
            if result:
                if result.role == "owner":
                    print(f"Name: {result.name}, Email: {result.email}, Role: {result.role}, SINPE: {result.sinpe_number}")
                else:
                    print(f"Name: {result.name}, Email: {result.email}, Role: {result.role}")
            else:
                print("⚠️ User not found.")
        else:
            print("❌ Invalid option.")

def delete_user():
    print("\n🗑️ Delete User")
    email_to_delete = input("Enter the email of the user to delete: ").strip()

    with engine.connect() as conn:
        user = conn.execute(select(users).where(users.c.email == email_to_delete)).fetchone()

        if not user:
            print("⚠️ User not found.")
            return

        print(f"\nAre you sure you want to delete the following user?")
        print(f"📧 Email: {user.email}")
        print(f"👤 Name: {user.name}")
        print(f"👥 Role: {user.role}")

        confirmation = input("Type 'yes' to confirm: ").strip().lower()
        if confirmation != "yes":
            print("❌ Deletion cancelled.")
            return

        delete_stmt = users.delete().where(users.c.email == email_to_delete)
        result = conn.execute(delete_stmt)

        if result.rowcount:
            print("✅ User deleted successfully.")
        else:
            print("⚠️ No user deleted.")

def run_join_query():
    print("\n📄 View Rentals by Owner or Visitor")

    print("1. Filter by Owner Email")
    print("2. Filter by Visitor Email")
    print("3. Show All Rentals")
    option = input("Choose an option (1-3): ").strip()

    email_filter = None
    role_filter = None

    if option == "1":
        email_filter = input("Enter the owner's email: ").strip()
        role_filter = "owner"
    elif option == "2":
        email_filter = input("Enter the visitor's email: ").strip()
        role_filter = "visitor"
    elif option == "3":
        pass  # no filters
    else:
        print("❌ Invalid option.")
        return

    stmt = (
        select(
            rentals.c.id,
            rentals.c.start_time,
            rentals.c.end_time,
            rentals.c.total_price,
            users.c.name.label("user_name"),
            users.c.role,
            parking_spaces.c.number.label("space_number"),
            parking_spaces.c.floor.label("floor"),
        )
        .select_from(
            rentals
            .join(users, rentals.c.visitor_id == users.c.id)
            .join(parking_spaces, rentals.c.space_id == parking_spaces.c.id)
            .join(users.alias("owners"), parking_spaces.c.owner_id == users.alias("owners").c.id)
        )
    )

    if email_filter and role_filter == "visitor":
        stmt = stmt.where(users.c.email == email_filter)
    elif email_filter and role_filter == "owner":
        owners = users.alias("owners")
        stmt = stmt.where(owners.c.email == email_filter)

    with engine.connect() as conn:
        results = conn.execute(stmt).fetchall()

        if not results:
            print("⚠️ No rentals found.")
            return

        for row in results:
            print(f"\n🆔 Rental ID: {row.id}")
            print(f"👤 Visitor: {row.user_name}")
            print(f"🏠 Owner Role: {row.role}")
            print(f"🅿️ Parking Space: {row.space_number} (Floor {row.floor})")
            print(f"⏱ Start: {row.start_time}")
            print(f"⏱ End: {row.end_time}")
            print(f"💰 Total Price: ₡{row.total_price}")

while True:
    print("\n🔹 URBN Escalante Parking - Menu Options 🔹")
    print("1. Insert data into a table")
    print("2. Update data in a table")
    print("3. Select data from a table")
    print("4. Delete data from a table")
    print("5. Run a JOIN query")
    print("0. Exit")

    option = input("Select an option: ")

    if option == "0":
        print("Exiting application.")
        break
    elif option == "1":
        insert_users() # Call the def to insert data:
        pass
    elif option == "2":
        update_users()
        pass
    elif option == "3":
        select_users()
        pass
    elif option == "4":
        delete_user()
        pass
    elif option == "5":
        # join_query()
        pass
    else:
        print("❌ Invalid option. Please try again.")