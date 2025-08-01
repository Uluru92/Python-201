'''
All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to 
print information about the film and category table.
'''
# I am using sakila-mv-schema.sql and sakila-mv-data.sql with MySQL Workbench

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
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

# Reflect the existing database... so we don't need to define all existing tables
metadata = MetaData()
metadata.reflect(bind=engine)

# Access the 'film' and 'category' tables
film_table = metadata.tables['film']
category_table = metadata.tables['category']

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Print some info from each table
with engine.connect() as conn:
    print("Films:")
    result = conn.execute(film_table.select()).fetchall()
    for row in result:
        print(row.title + ": "+row.description)

    print("\nCategories:")
    result = conn.execute(category_table.select()).fetchall()
    for row in result:
        last_update = row.last_update.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{row.category_id}: {row.name} - Last updated on {last_update}")