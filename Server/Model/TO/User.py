from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

from Server.Model.DA import Base


class User(Base, dict):
    __tablename__ = 'users'
    id = Column('user_id', Integer, Sequence('user_id_seq'), primary_key=True)
    firstName = Column('user_firstName', String(50))
    lastName = Column('user_lastName', String(50))
    email = Column('user_email', String(50), unique=True)
    username = Column('user_username', String(50), unique=True)
    password = Column('user_password', String(50))
    questions = relationship('Question', backref="questionUser", cascade="all, delete, delete-orphan")
    answers = relationship('Answer', backref="answerUser", cascade="all, delete, delete-orphan")

    def __init__(self, firstName=None, lastName=None, email=None, username=None, password=None, userType=None,
                 questions=None, answers=None):
        if answers is None:
            answers = []
        if questions is None:
            questions = []
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.password = password
        self.userType = userType
        self.questions = questions
        self.answers = answers
        dict.__init__(self, firstName=self.firstName, lastName=self.lastName, email=self.email, username=self.username,
                      password=self.password, userType=self.userType, questions=self.questions, answers=self.answers)
