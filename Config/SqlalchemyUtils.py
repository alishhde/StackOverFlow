from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///E:\\Network Project\\Stackoverflow\\StackoverfolwDB.db', echo=True)
Base = declarative_base()
