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
from sqlalchemy import create_engine, text, select, insert, ForeignKey, Boolean, Table, Column, MetaData
import os

# API info
base_url_users = "http://demo.codingnomads.co:8080/tasks_api/users"
base_url_task = "http://demo.codingnomads.co:8080/tasks_api/tasks"
response_users = requests.get(base_url_users)
response_tasks = requests.get(base_url_task)

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
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{MYSQL_DB}"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create the new database in MySQL Workbench
db_name = "users_and_tasks_db"