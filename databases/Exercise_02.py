'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice: DONE

- Select all the actors and the films they have been in: DONE

- Select all the actors that have appeared in a category of a comedy of your choice: DONE

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''

from sqlalchemy import create_engine, MetaData, select
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
actor_table = metadata.tables['actor']
film_actor_table = metadata.tables['film_actor']
film_table = metadata.tables['film']
film_category_table = metadata.tables['film_category']
category_table = metadata.tables['category']

# Create session
Session = sessionmaker(bind=engine)
session = Session()

with engine.connect() as conn:
    # Select all the actors with the first name of your choice
    print("\nActors with the first name Frances:")
    result = conn.execute(actor_table.select()).fetchall()
    for row in result:
        print(row.first_name +" "+row.last_name) if row.first_name == "FRANCES" else None

    # Select all the actors and the films they have been in
    print("\nAll actors and the films they have been in:")

    query = select(
        actor_table.c.first_name,
        actor_table.c.last_name,
        film_table.c.title
        ).select_from(
            actor_table
            .join(film_actor_table, actor_table.c.actor_id == film_actor_table.c.actor_id)
            .join(film_table, film_actor_table.c.film_id == film_table.c.film_id)
            )

    result = conn.execute(query).fetchall()

    for row in result:
        print(f"{row.first_name} {row.last_name} - {row.title}")

    # Select all the actors that have appeared in a category of a comedy of your choice
    print("\nActors appeared in Animation:")
    query = select(
        actor_table.c.first_name,
        actor_table.c.last_name,
        film_table.c.title,
        category_table.c.name,
        ).select_from(
            actor_table
            .join(film_actor_table, actor_table.c.actor_id == film_actor_table.c.actor_id)
            .join(film_table, film_actor_table.c.film_id == film_table.c.film_id)
            .join(film_category_table, film_table.c.film_id == film_category_table.c.film_id)
            .join(category_table, category_table.c.category_id == film_category_table.c.category_id)
            ).where(
                category_table.c.name == "Animation")

    result = conn.execute(query).fetchall()

    for row in result:
        print(f"{row.first_name} {row.last_name} - {row.title} - {row.name}")