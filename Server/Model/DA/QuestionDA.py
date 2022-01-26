from Server.Model.DA import object_as_dict, session
from Server.Model.TO.Question import Question
from Server.Model.TO.User import User


def insert(question, userId):
    session.add(question)
    user = session.query(User).filter(userId)
    user.questions.append(question)
    session.commit()
    return 1


def select():
    questions = []
    for question in session.query(Question).all():
        questions.append(object_as_dict(question))
    session.commit()
    return questions


def update(question, userId):
    session.query(Question).filter(question.id).update(
        {Question.id: question.id, Question.header: question.header, Question.body: question.body,
         Question.voteCount: question.voteCount, Question.userId: question.userId, Question.answers: question.answers,
         Question.comments: question.comments},
        synchronize_session=False)
    questions = session.query(User).filter(userId).questions
    for questioni in questions:
        if questioni.id == question.id:
            questions[questioni.index()] = question
    session.commit()
    return 1


def delete(question, userId):
    session.query(Question).filter(question.id).delete()
    user = session.query(User).filter(userId)
    user.questions.remove(question)
    session.commit()
    return 1
