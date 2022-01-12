from Config.SqlalchemyUtils import session
from Model.TO.User import User


def insert(user):
    session.add(user)
    session.commit()
    return 1


def select():
    users = session.query(User).all()
    session.commit()
    return users


def update(user):
    session.query(User).filter(user.id).update(
        {User.id: user.id, User.firstName: user.firstName, User.lastName: user.lastName,
         User.email: user.email, User.username: user.username,
         User.password: user.password, User.userType: user.userType,
         User.questions: user.questions, User.answers: user.answers,
         User.comments: user.comments},
        synchronize_session=False)
    session.commit()
    return 1


def delete(userId):
    session.query(User).filter(userId).delete()
    session.commit()
    return 1
