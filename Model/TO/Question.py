from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from Config.SqlalchemyUtils import Base


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
