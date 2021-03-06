from Server.Model.DA import session, object_as_dict
from Server.Model.TO.Answer import Answer
from Server.Model.TO.User import User


def insert(answer, userId):
    session.add(answer)
    user = session.query(User).filter(userId)
    user.answers.append(answer)
    session.commit()
    return 1


def select():
    answers = []
    for answer in session.query(Answer).all():
        answers.append(object_as_dict(answer))
    session.commit()
    return answers


def update(answer, userId):
    session.query(Answer).filter(answer.id).update(
        {Answer.id: answer.id, Answer.body: answer.body, Answer.voteCount: answer.voteCount,
         Answer.userId: answer.userId, Answer.questionId: answer.questionId, Answer.comments: answer.comments},
        synchronize_session=False)
    answers = session.query(User).filter(userId).answers
    for answeri in answers:
        if answeri.id == answer.id:
            answers[answeri.index()] = answer
    session.commit()
    return 1


def delete(answer, userId):
    session.query(Answer).filter(answer.id).delete()
    user = session.query(User).filter(userId)
    user.answers.remove(answer)
    session.commit()
    return 1
