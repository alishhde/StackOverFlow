from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from Server.Config.SqlalchemyUtils import Base


class Answer(Base):
    __tablename__ = 'answers'
    id = Column('answer_id', Integer, Sequence('answer_id_seq'), primary_key=True)
    body = Column('answer_body', String(50))
    voteCount = Column('answer_voteCount', String(50))
    userId = Column('answer_userId', Integer, ForeignKey('users.user_id'))
    questionId = Column('answer_questionId', Integer, ForeignKey('questions.question_id'))
    comments = relationship('Comment', cascade="all, delete-orphan")

    # def __init__(self, comments):
    #     self.comments = comments
