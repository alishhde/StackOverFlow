from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///D:\\My Works\\Projects\\Python Projects\\Project StackOverFlow\\StackoverfolwDB.db', echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
