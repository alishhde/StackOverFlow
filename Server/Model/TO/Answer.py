from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

from Server.Model.DA import Base


class Answer(Base, dict):
    __tablename__ = 'answers'
    id = Column('answer_id', Integer, Sequence('answer_id_seq'), primary_key=True, unique=True)
    body = Column('answer_body', String(50))
    voteCount = Column('answer_voteCount', String(50))
    userId = Column('answer_userId', Integer, ForeignKey('users.user_id'))
    questionId = Column('answer_questionId', Integer, ForeignKey('questions.question_id'))

    def __init__(self, body=None, voteCount=None, userId=None, questionId=None):
        self.body = body
        self.voteCount = voteCount
        self.userId = userId
        self.questionId = questionId
        dict.__init__(self, body=self.body, voteCount=self.voteCount, userId=self.userId, questionId=self.questionId)
