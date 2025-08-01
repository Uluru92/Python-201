'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.
'''

from sqlalchemy import create_engine, MetaData, select, update
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

# Access required tables
film_table = metadata.tables['film']

# Create session
Session = sessionmaker(bind=engine)
session = Session()

with engine.connect() as conn:
    # Update films rental_duration value of 10 if the length of the movie is more than 150.
    print("\nfilms updated:")
    query = update(
        film_table
        ).where(
            film_table.c.length >= 150
            ).values({film_table.c.rental_duration:10})
    result = conn.execute(query)

    #Show films updated
    query = select(
        film_table.c.title,
        film_table.c.length,
        film_table.c.rental_duration,
    ).select_from(
        film_table
    ).where(
    film_table.c.length >= 150
    )

    result = conn.execute(query).fetchall()
    for row in result:
        print(f"{row.title} - Length: {row.length} - Rental Duration: {row.rental_duration}")