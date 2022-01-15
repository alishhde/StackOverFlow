from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

from Server.Config.SqlalchemyUtils import Base


class Comment(Base):
    __tablename__ = 'comments'
    id = Column('comment_id', Integer, Sequence('comment_id_seq'), primary_key=True)
    body = Column('comment_body', String(50))
    voteCount = Column('comment_voteCount', String(50))
    userId = Column('comment_userId', Integer, ForeignKey('users.user_id'))
    questionId = Column('comment_questionId', Integer, ForeignKey('questions.question_id'))
    answerId = Column('comment_answerId', Integer, ForeignKey('answers.answer_id'))
