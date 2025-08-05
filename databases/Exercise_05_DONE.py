'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

import requests
from sqlalchemy import create_engine, text, select, insert, Integer,String, DateTime, ForeignKey, Boolean, Table, Column, MetaData
import os
from datetime import datetime

# API info
base_url_users = "http://demo.codingnomads.co:8080/tasks_api/users"
base_url_task = "http://demo.codingnomads.co:8080/tasks_api/tasks"
response_users = requests.get(base_url_users).json()
response_tasks = requests.get(base_url_task).json()

print("Let's GET all users and all of their task...\n")

from dotenv import load_dotenv

load_dotenv()

# Info to connect to MySQL Workbench
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")
MYSQL_DB = os.getenv("MYSQL_DB_USERS_AND_TASKS")

# Build database URL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"

# Create the engine
engine_to_conect = create_engine(DATABASE_URL)

# Create the new database in MySQL Workbench
db_name = "users_tasks_db"

with engine_to_conect.begin() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
    print(f"\nDatabase '{db_name}' created or already exists.")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{db_name}"

engine = create_engine(DATABASE_URL)

metadata = MetaData()

# create 2 tables: 
users_table = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(100), nullable=False, unique=True),
    Column("first_name", String(100), nullable=False),
    Column("last_name", String(100), nullable=False),
    Column("created_at", DateTime, nullable=False),
    Column("updated_at", DateTime, nullable=False)
)

tasks_table = Table(
    "tasks", metadata,
    Column("id", Integer, primary_key=True),
    Column("userId", Integer, ForeignKey("users.id")),
    Column("name",  String(100), nullable=False),
    Column("description",  String(100), nullable=False),
    Column("createdAt", DateTime, nullable=False),
    Column("updatedAt", DateTime, nullable=False),
    Column("completed", Boolean, default=False),
)

metadata.create_all(engine)

def insert_users():
    users_data = response_users["data"]

    with engine.begin() as conn:
        for user in users_data:
            conn.execute(insert(users_table).prefix_with("IGNORE").values(
                id=user["id"],
                email=user["email"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                created_at=datetime.fromtimestamp(user["created_at"] / 1000),
                updated_at=datetime.fromtimestamp(user["updated_at"] / 1000)
            ))
    print(f"\n✅ {len(users_data)} usuarios insertados correctamente.")

def insert_tasks():
    tasks_data = response_tasks["data"]

    with engine.begin() as conn:
        for task in tasks_data:
            conn.execute(insert(tasks_table).prefix_with("IGNORE").values(
                id=task["id"],
                userId=task["userId"],
                name=task["name"],
                description=task["description"],
                createdAt=datetime.fromtimestamp(task["createdAt"] / 1000),  # camelCase aquí
                updatedAt=datetime.fromtimestamp(task["updatedAt"] / 1000),  # camelCase aquí
                completed=task["completed"]
            ))
    print(f"\n✅ {len(tasks_data)} tareas insertadas correctamente.")

insert_users()
insert_tasks()