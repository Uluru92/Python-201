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

from sqlalchemy import create_engine, func, text, MetaData,Table, Column, Integer, String, Enum, DateTime, MetaData

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

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("email", String(100), nullable=False, unique=True),
    Column("role", Enum("owner", "visitor"), nullable=False),
    Column("created_at", DateTime, server_default=func.now())
)

while True:
    print("\n🔹 URBN Escalante Parking - Menu Options 🔹")
    print("1. Create tables")
    print("2. Insert data into a table")
    print("3. Update data in a table")
    print("4. Select data from a table")
    print("5. Delete data from a table")
    print("6. Run a JOIN query")
    print("0. Exit")

    option = input("Select an option: ")

    if option == "1":
                
        pass
    elif option == "2":
        # Call function to insert data
        pass
    elif option == "3":
        # Call function to update data
        pass
    elif option == "4":
        # Call function to select data
        pass
    elif option == "5":
        # Call function to delete data
        pass
    elif option == "6":
        # Call function to run join
        pass
    elif option == "0":
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")