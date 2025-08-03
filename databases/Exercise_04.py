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
def insert_data():
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

# update data in each table (as a function to call it later): 
def update_users_table():
    print("\n🔄 Update User Data")
    email_to_update = input("Enter the email of the user to update: ").strip()
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
                    if len(sinpe) != 8 or not sinpe.isdigit():
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
                # If new role is visitor, no SINPE check required
                stmt = (
                    users.update()
                    .where(users.c.email == email_to_update)
                    .values({users.c.role: new_value})
                )

            updated = conn.execute(stmt)
            if updated.rowcount:
                print("✅ Role updated successfully.")
            else:
                print("⚠️ No user found.")

    elif option == "4":
        new_value = input("Enter the new SINPE number (XXXXXXXX): ").strip()
        if len(new_value) != 8 or not sinpe.isdigit():
            print("❌ Invalid SINPE format.")
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
        insert_data() # Call the def to insert data:
        pass
    elif option == "2":
        # update_data()
        pass
    elif option == "3":
        # select_data()
        pass
    elif option == "4":
        # delete_data()
        pass
    elif option == "5":
        # join_query()
        pass
    else:
        print("❌ Invalid option. Please try again.")