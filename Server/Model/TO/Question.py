from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from Server.Model.DA import Base


class Question(Base, dict):
    __tablename__ = 'questions'
    id = Column('question_id', Integer, Sequence('question_id_seq'), primary_key=True, unique=True)
    header = Column('question_header', String(50))
    body = Column('question_body', String(50))
    voteCount = Column('question_voteCount', Integer)
    userId = Column('question_userId', Integer, ForeignKey('users.user_id'))
    answers = relationship('Answer', backref="user", cascade="all, delete, delete-orphan")

    def __init__(self, header=None, body=None, voteCount=None, userId=None, answers=None):
        if answers is None:
            answers = []
        self.header = header
        self.body = body
        self.voteCount = voteCount
        self.userId = userId
        self.answers = answers
        dict.__init__(self, header=self.header, body=self.body, voteCount=self.voteCount, userId=self.userId,
                      answers=self.answers)
