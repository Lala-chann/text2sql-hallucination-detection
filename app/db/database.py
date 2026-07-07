#TODO: create_engine function creates a CONNECTION object to you database
from sqlalchemy import create_engine

#TODO: sessionmaker is function that knows how you interact with the database, you use it to QUERY, INSERT, UPDTATE, DELETE
#TODO: declarative_base creates a base class that all your ORM models will map directly to database tables.
from sqlalchemy.orm import sessionmaker, declarative_base

#connect with config file from app folder
from app.config import settings

#TODO: engine creates a connection to the database using the Database URL based on .env file that you set in which database will be using
engine = create_engine(settings.DATABASE_URL)

#TODO: sessionmaker is factory for creating new session objects. bind=engine means connect to database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#TODO: The foundation for all your ORM models.
Base = declarative_base()