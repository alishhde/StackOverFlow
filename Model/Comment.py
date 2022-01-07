from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

from Config.SqlalchemyUtils import Base, engine


class Comment(Base):
    __tablename__ = 'comments'
    id = Column('comment_id', Integer, Sequence('comment_id_seq'), primary_key=True)
    body = Column('comment_body', String(50))
    voteCount = Column('comment_voteCount', String(50))
    userId = Column(Integer, ForeignKey('User.id'))
    questionId = Column(Integer, ForeignKey('Question.id'))
    answerId = Column(Integer, ForeignKey('Answer.id'))


Base.metadata.create_all(engine)
