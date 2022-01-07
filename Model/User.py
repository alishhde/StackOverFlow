from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

from Config.SqlalchemyUtils import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer, Sequence('user_id_seq'), primary_key=True)
    firstName = Column('user_firstName', String(50))
    lastName = Column('user_lastName', String(50))
    email = Column('user_email', String(50))
    username = Column('user_username', String(50))
    password = Column('user_password', String(50))
    userType = Column('user_userType', String(50))
    questions = relationship('Question')
    answers = relationship('Answer')
    comments = relationship('Comment')


Base.metadata.create_all(engine)
