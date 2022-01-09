from Config.SqlalchemyUtils import Base, engine
from Model.TO.Answer import Answer
from Model.TO.Comment import Comment
from Model.TO.Question import Question
from Model.TO.User import User

user = User()
question = Question()
answer = Answer()
comment = Comment()

Base.metadata.create_all(engine, checkfirst=True)
