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

from sqlalchemy import create_engine, func, text, select, insert, ForeignKey, Boolean, MetaData,Table, Column, Integer, String, Enum, DateTime, MetaData
import re
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
    Column("number", String(10), primary_key=True),
    Column("owner_id", Integer, ForeignKey("users.id")),
    Column("floor", Integer, nullable=False),
    Column("is_available", Boolean, default=True),
    Column("price_per_hour", Integer, nullable=False),
    Column("is_deleted", Boolean, default=False)
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

# def () for users menu:
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

def is_valid_sinpe(sinpe):
    return sinpe.isdigit() and len(sinpe) == 8

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

    owners = users.alias("owners")

    stmt = (
        select(
            rentals.c.id,
            rentals.c.start_time,
            rentals.c.end_time,
            rentals.c.total_price,
            users.c.name.label("visitor_name"),
            users.c.role.label("visitor_role"),
            parking_spaces.c.number.label("space_number"),
            parking_spaces.c.floor.label("floor"),
            owners.c.name.label("owner_name"),
            owners.c.email.label("owner_email"),
        )
        .select_from(
            rentals
            .join(users, rentals.c.visitor_id == users.c.id)  # Visitor join
            .join(parking_spaces, rentals.c.space_number == parking_spaces.c.number)  # FK now space_number
            .join(owners, parking_spaces.c.owner_id == owners.c.id)  # Owner join
        )
        .where(parking_spaces.c.is_deleted == False)
    )

    if email_filter and role_filter == "visitor":
        stmt = stmt.where(users.c.email == email_filter)
    elif email_filter and role_filter == "owner":
        stmt = stmt.where(owners.c.email == email_filter)

    with engine.connect() as conn:
        results = conn.execute(stmt).fetchall()

        if not results:
            print("⚠️ No rentals found.")
            return

        for row in results:
            print(f"\n🆔 Rental ID: {row.id}")
            print(f"👤 Visitor: {row.visitor_name} ({row.visitor_role})")
            print(f"🏠 Owner: {row.owner_name} ({row.owner_email})")
            print(f"🅿️ Parking Space: {row.space_number} (Floor {row.floor})")
            print(f"⏱ Start: {row.start_time}")
            print(f"⏱ End: {row.end_time}")
            print(f"💰 Total Price: ₡{row.total_price}")

def main_menu():
    while True:
        print("\n📋URBN Escalante - Main Menu")
        print("1. Manage Users")
        print("2. Manage Parking Spaces")
        print("3. Manage Rentals")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            users_menu()
        elif choice == "2":
            parking_spaces_menu()
        elif choice == "3":
            rentals_menu()
        elif choice == "4":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def users_menu():
    while True:
        print("\n👤 Users Menu")
        print("1. Insert data")
        print("2. Update data")
        print("3. Select data")
        print("4. Delete data")
        print("5. View Rentals by Owner or Visitor")
        print("0. Exit")

        option = input("Select an option: ")

        if option == "0":
            print("Exiting application.")
            break
        elif option == "1":
            insert_users()
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
            run_join_query()
            pass
        else:
            print("❌ Invalid option. Please try again.")

# def () for parking spaces menu:
def is_valid_parking_number(parking_number):
    pattern = r"^N\d{1,2}P\d{1,2}$"
    return re.match(pattern, parking_number.upper()) is not None

def insert_parking_space():
    print("\n➕ Add Parking Space")
    try:
        owner_email = input("Enter owner's email: ").strip()
        with engine.connect() as conn:
            # Verificar que el owner existe y es "owner"
            owner = conn.execute(
                select(users.c.id, users.c.role).where(users.c.email == owner_email)
            ).fetchone()
            if not owner:
                print("❌ No user found with that email.")
                return
            if owner.role != "owner":
                print("❌ This user is not registered as an 'owner'.")
                return

            floor = input("Enter floor number: ").strip()
            if not floor.isdigit():
                print("❌ Floor must be a number.")
                return

            number = input("Enter parking space number (e.g. N3P10): ").strip().upper()
            if not number:
                print("❌ Parking space number cannot be empty.")
                return

            # Validar formato del número (ejemplo: N3P10)
            if not re.match(r"^N\d+P\d+$", number):
                print("❌ Invalid parking space number format. Example: N3P10")
                return

            price_input = input("Enter price per hour (in colones): ").strip()
            if not price_input.isdigit():
                print("❌ Price must be a number.")
                return
            price_per_hour = int(price_input)

            # Chequear si existe un espacio con ese número, sea eliminado o no
            existing = conn.execute(
                select(parking_spaces).where(parking_spaces.c.number == number)
            ).fetchone()

            if existing:
                if existing.is_deleted:
                    print(f"⚠️ Parking space '{number}' was previously deleted.")
                    restore = input("Do you want to restore it? (yes/no): ").strip().lower()
                    if restore == "yes":
                        stmt = (
                            parking_spaces.update()
                            .where(parking_spaces.c.number == number)
                            .values(
                                owner_id=owner.id,
                                floor=int(floor),
                                is_available=True,
                                price_per_hour=price_per_hour,
                                is_deleted=False,
                            )
                        )
                        conn.execute(stmt)
                        print(f"✅ Parking space '{number}' restored and updated successfully.")
                    else:
                        print("Operation cancelled.")
                    return
                else:
                    print("❌ A parking space with this number already exists.")
                    return

            # Si no existe, insertamos nuevo
            stmt = insert(parking_spaces).values(
                owner_id=owner.id,
                floor=int(floor),
                number=number,
                is_available=True,
                price_per_hour=price_per_hour,
                is_deleted=False,
            )
            conn.execute(stmt)
            print("✅ Parking space added successfully.")

    except Exception as e:
        print(f"❌ Error inserting parking space: {e}")

def list_parking_spaces():
    print("\n📋 Parking Spaces List")
    print("1. Show all")
    print("2. Show only available")
    print("3. Show only occupied")

    choice = input("Choose an option (1-3): ").strip()

    filter_condition = None

    if choice == "2":
        filter_condition = parking_spaces.c.is_available == True
    elif choice == "3":
        filter_condition = parking_spaces.c.is_available == False
    elif choice != "1":
        print("❌ Invalid option.")
        return

    try:
        with engine.connect() as conn:
            stmt = (
                select(
                    parking_spaces.c.id,
                    users.c.name.label("owner_name"),
                    parking_spaces.c.floor,
                    parking_spaces.c.number,
                    parking_spaces.c.is_available,
                    parking_spaces.c.price_per_hour
                )
                .select_from(
                    parking_spaces.join(users, parking_spaces.c.owner_id == users.c.id)
                )
                .where(parking_spaces.c.is_deleted == False)
                .order_by(parking_spaces.c.floor, parking_spaces.c.number)
            )

            if filter_condition is not None:
                stmt = stmt.where(filter_condition)

            results = conn.execute(stmt).fetchall()

            if not results:
                print("ℹ️ No parking spaces found with that filter.")
                return

            for row in results:
                availability = "✅ Available" if row.is_available else "❌ Occupied"
                print(f"""
                    🅿️ ID: {row.id}
                    👤 Owner: {row.owner_name}
                    🏢 Floor: {row.floor}
                    🔢 Number: {row.number}
                    💰 Price/hr: ₡{row.price_per_hour}
                    📶 Status: {availability}
                    -------------------------
                    """)

    except Exception as e:
        print(f"❌ Error retrieving parking spaces: {e}")

def update_parking_space():
    print("\n🔄 Update Parking Space")
    space_number = input("Enter the parking space number (e.g. N3P10): ").strip().upper()
    if not is_valid_parking_number(space_number):
        print("❌ Invalid parking number format. Use format like N3P10.")
        return

    with engine.connect() as conn:
        # Buscar espacio que NO esté eliminado
        space = conn.execute(
            select(parking_spaces)
            .where(parking_spaces.c.number == space_number, parking_spaces.c.is_deleted == False)
        ).fetchone()
        if not space:
            print("⚠️ Parking space not found.")
            return

        if not space.is_available:
            print("⛔ This parking space is currently occupied. You can only update the owner.")
            choice = input("Do you want to update the owner (via email)? (yes/no): ").strip().lower()
            if choice != "yes":
                print("❌ Update cancelled.")
                return

            new_owner_email = input("Enter new owner's email: ").strip()
            owner_check = conn.execute(
                select(users.c.id)
                .where(users.c.email == new_owner_email)
            ).fetchone()
            if not owner_check:
                print("❌ No user found with that email.")
                return
            new_owner_id = owner_check.id

            stmt = (
                parking_spaces.update()
                .where(parking_spaces.c.number == space_number, parking_spaces.c.is_deleted == False)
                .values(owner_id=new_owner_id)
            )
            conn.execute(stmt)
            print("✅ Owner updated successfully.")
            return

        # Espacio disponible, se permite actualización completa
        print("\nWhat would you like to update?")
        print("1. Owner (via email)")
        print("2. Floor")
        print("3. Number")
        print("4. Price per Hour")
        print("5. Mark as unavailable")

        option = input("Choose an option (1-5): ").strip()

        update_column = None
        new_value = None

        if option == "1":
            new_owner_email = input("Enter new owner's email: ").strip()
            owner_check = conn.execute(
                select(users.c.id)
                .where(users.c.email == new_owner_email)
            ).fetchone()
            if not owner_check:
                print("❌ No user found with that email.")
                return
            update_column = parking_spaces.c.owner_id
            new_value = owner_check.id

        elif option == "2":
            new_value_input = input("Enter new floor (integer): ").strip()
            if not new_value_input.isdigit():
                print("❌ Floor must be an integer.")
                return
            update_column = parking_spaces.c.floor
            new_value = int(new_value_input)

        elif option == "3":
            new_number = input("Enter new parking number (e.g. N3P10): ").strip().upper()
            if not is_valid_parking_number(new_number):
                print("❌ Invalid parking number format. Use format like N3P10.")
                return

            # Verificar que no exista otro espacio con ese número y que no sea el mismo que estamos editando
            existing = conn.execute(
                select(parking_spaces)
                .where(
                    parking_spaces.c.number == new_number,
                    parking_spaces.c.is_deleted == False,
                    parking_spaces.c.number != space_number  # Evitar choque con el mismo
                )
            ).fetchone()

            if existing:
                print("❌ That number is already in use.")
                return

            update_column = parking_spaces.c.number
            new_value = new_number

        elif option == "4":
            new_price_input = input("Enter new price per hour (₡): ").strip()
            if not new_price_input.isdigit():
                print("❌ Price must be an integer.")
                return
            update_column = parking_spaces.c.price_per_hour
            new_value = int(new_price_input)

        elif option == "5":
            update_column = parking_spaces.c.is_available
            new_value = False

        else:
            print("❌ Invalid option.")
            return

        try:
            stmt = (
                parking_spaces.update()
                .where(parking_spaces.c.number == space_number, parking_spaces.c.is_deleted == False)
                .values({update_column: new_value})
            )
            result = conn.execute(stmt)
            if result.rowcount:
                print("✅ Parking space updated successfully.")
            else:
                print("⚠️ Update failed.")
        except Exception as e:
            print(f"❌ Error: {e}")

def delete_parking_space():
    print("\n🗑️ Delete Parking Space")
    number = input("Enter parking space number to delete (e.g. N3P10): ").strip().upper()

    if not is_valid_parking_number(number):
        print("❌ Invalid parking space number format. Use something like N3P10.")
        return

    with engine.connect() as conn:
        # Buscar espacio que no esté eliminado
        space = conn.execute(
            select(parking_spaces)
            .where(parking_spaces.c.number == number, parking_spaces.c.is_deleted == False)
        ).fetchone()

        if not space:
            print("❌ Parking space not found or already deleted.")
            return

        if not space.is_available:
            print("❌ Cannot delete. This parking space is currently occupied.")
            return

        confirm = input(f"⚠️ Are you sure you want to delete parking space {number}? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("❌ Deletion cancelled.")
            return

        # Soft delete: marcar como eliminado
        stmt = (
            parking_spaces.update()
            .where(parking_spaces.c.number == number)
            .values(is_deleted=True)
        )
        result = conn.execute(stmt)

        if result.rowcount:
            print("✅ Parking space deleted (soft) successfully.")
        else:
            print("⚠️ Something went wrong. No space deleted.")


def parking_spaces_menu():
    while True:
        print("\n🚗 Parking Spaces Menu")
        print("1. Add Parking Space")
        print("2. List Parking Spaces")
        print("3. Update Parking Space")
        print("4. Delete Parking Space")
        print("5. Back to Main Menu")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            insert_parking_space()
        elif choice == "2":
            list_parking_spaces()
        elif choice == "3":
            update_parking_space()
        elif choice == "4":
            delete_parking_space()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice.")

def rentals_menu():
    while True:
        print("\n📅 Rentals Menu")
        print("1. Add Rental")
        print("2. List Rentals")
        print("3. Update Rental")
        print("4. Delete Rental")
        print("5. Back to Main Menu")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_rental()
        elif choice == "2":
            list_rentals()
        elif choice == "3":
            update_rental()
        elif choice == "4":
            delete_rental()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice.")
