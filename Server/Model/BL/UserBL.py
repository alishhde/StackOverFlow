from Server.Model.DA import UserDA


def verifyUser(username, inputPassword):
    accepted = 0
    try:
        accepted = UserDA.verify(username, inputPassword)
    except Exception as e:
        print("-----verifyUser-----")
        print(e)
        print("-----verifyUser-----")
    return accepted


def insertUser(user):
    rowsAffected = 0
    try:
        rowsAffected = UserDA.insert(user)
    except Exception as e:
        print("-----insertUser-----")
        print(e)
        print("-----insertUser-----")
    return rowsAffected


def selectUser(username):
    user = None
    try:
        user = UserDA.select(username)
    except Exception as e:
        print("-----selectUser-----")
        print(e)
        print("-----selectUser-----")
    return user


def updateUser(user):
    rowsAffected = 0
    try:
        rowsAffected = UserDA.update(user)
    except Exception as e:
        print("-----updateUser-----")
        print(e)
        print("-----updateUser-----")
    return rowsAffected


def deleteUser(userId):
    rowsAffected = 0
    try:
        rowsAffected = UserDA.delete(userId)
    except Exception as e:
        print("-----deleteUser-----")
        print(e)
        print("-----deleteUser-----")
    return rowsAffected
