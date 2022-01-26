from Server.Model.DA import session, object_as_dict
from Server.Model.TO.User import User


def verify(username, inputPassword):
    password = session.query(User.password).where(User.username == username).first()
    session.commit()
    if inputPassword == password[0]:
        return 1
    else:
        return 0


def insert(user):
    session.add(user)
    session.commit()
    return 1


def select(username):
    user = session.query(User).filter(User.username == username).first()
    session.commit()
    return object_as_dict(user)


def update(user):
    session.query(User).filter(User.id == user.id).update(
        {User.id: user.id, User.firstName: user.firstName, User.lastName: user.lastName,
         User.email: user.email, User.username: user.username,
         User.password: user.password, User.userType: user.userType,
         User.questions: user.questions, User.answers: user.answers,
         User.comments: user.comments},
        synchronize_session=False)
    session.commit()
    return 1


def delete(userId):
    user = session.query(User).filter(User.id == userId).first()
    session.delete(user)
    session.commit()
    return 1
