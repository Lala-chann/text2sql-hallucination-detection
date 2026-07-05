#Import the function that creates a database = Verilenler bazasina qosulmaq ucun "engine" adli funksiya
from sqlalchemy import create_engine

#Build session objects to interact with the database and declarative_base creates the Base class that all models inherit from
from sqlalchemy.orm import sessionmaker, declarative_base

#connect with config file from app folder
from app.config import settings

#Creates the actual data base connection using the URL = data base url qosulmaq ucundur url burda evvelceden .env yazilib
engine = create_engine(settings.DATABASE_URL)

#defines the session factory = autocommit deyisiklikleri ozun commit etmleisen, autoflush commit etmeyene qeder deyisiklikler avtomati yazilmir, bin ise sesssin hemin engine baglayir
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#bugun orm moddeleri burdan miras alir
Base = declarative_base()