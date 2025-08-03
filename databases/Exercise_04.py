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

from sqlalchemy import create_engine, func, text, ForeignKey, Boolean, MetaData,Table, Column, Integer, String, Enum, DateTime, MetaData

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
    Column("role", Enum("owner", "visitor"), nullable=False),
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

# insert data to each table: For this step, I created a def to insert later on my tables
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