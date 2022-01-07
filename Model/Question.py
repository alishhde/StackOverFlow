from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from Config.SqlalchemyUtils import Base, engine


class Question(Base):
    __tablename__ = 'questions'
    id = Column('question_id', Integer, Sequence('question_id_seq'), primary_key=True)
    header = Column('question_header', String(50))
    body = Column('question_body', String(50))
    voteCount = Column('question_voteCount', String(50))
    userId = Column(Integer, ForeignKey('User.id'))
    answers = relationship('Answer')
    comments = relationship('Comment')


Base.metadata.create_all(engine)
