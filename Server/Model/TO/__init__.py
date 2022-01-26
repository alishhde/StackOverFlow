from Server.Model.DA import Base, engine
from Server.Model.TO.Answer import Answer
from Server.Model.TO.Question import Question
from Server.Model.TO.User import User

Base.metadata.create_all(engine)
