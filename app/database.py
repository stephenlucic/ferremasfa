from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



database_url ="mysql+pymysql://root:@localhost:3306/ferremas_db"  # "sqlite:///:memory:" "mysql+pymysql://root:@localhost:3306/ferremas_db"

engine= create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
