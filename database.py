import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database



# SQLAlchemy database URL for PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/task_db"

engine = create_engine(DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)
    print("Database created!")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def create_database():
#     try:
#         # Connect to PostgreSQL server (default database 'postgres')
#         conn = psycopg2.connect(
#             dbname="postgres",
#             user="postgres",
#             password="postgres",
#             host="localhost",
#             port="5432"
#         )
#         conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#         cursor = conn.cursor()

#         # Create database
#         cursor.execute("CREATE DATABASE task_db")
#         print("Database 'task_db' created successfully!")
        
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(f"Error creating database: {e}")

# if __name__ == "__main__":
#     create_database()