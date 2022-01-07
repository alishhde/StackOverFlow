from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from Config.SqlalchemyUtils import Base, engine


class Answer(Base):
    __tablename__ = 'answers'
    id = Column('answer_id', Integer, Sequence('answer_id_seq'), primary_key=True)
    body = Column('answer_body', String(50))
    voteCount = Column('answer_voteCount', String(50))
    userId = Column(Integer, ForeignKey('User.id'))
    questionId = Column(Integer, ForeignKey('Question.id'))
    comments = relationship('Comment')


Base.metadata.create_all(engine)
