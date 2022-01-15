from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

from Server.Config.SqlalchemyUtils import Base


class User(Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer, Sequence('user_id_seq'), primary_key=True)
    firstName = Column('user_firstName', String(50))
    lastName = Column('user_lastName', String(50))
    email = Column('user_email', String(50))
    username = Column('user_username', String(50))
    password = Column('user_password', String(50))
    userType = Column('user_userType', String(50))
    questions = relationship('Question', cascade="all, delete-orphan")
    answers = relationship('Answer', cascade="all, delete-orphan")
    comments = relationship('Comment', cascade="all, delete-orphan")

    # def __init__(self, questions, answers, comments):
    #     self.questions = questions
    #     self.answers = answers
    #     self.comments = comments
