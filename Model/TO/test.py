from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
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
    questions = relationship('Question', cascade="all, delete-orphan")
    answers = relationship('Answer', cascade="all, delete-orphan")
    comments = relationship('Comment', cascade="all, delete-orphan")

    # def __init__(self, questions, answers, comments):
    #     self.questions = questions
    #     self.answers = answers
    #     self.comments = comments


class Question(Base):
    __tablename__ = 'questions'
    id = Column('question_id', Integer, Sequence('question_id_seq'), primary_key=True)
    header = Column('question_header', String(50))
    body = Column('question_body', String(50))
    voteCount = Column('question_voteCount', Integer)
    userId = Column('question_userId', Integer, ForeignKey('users.user_id'))
    answers = relationship('Answer', cascade="all, delete-orphan")
    comments = relationship('Comment', cascade="all, delete-orphan")

    # def __init__(self, answers, comments):
    #     self.answers = answers
    #     self.comments = comments


Base.metadata.create_all(engine)
