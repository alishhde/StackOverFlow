from Model.DA import UserDA


def insertUser(user):
    rowsAffected = 0
    try:
        rowsAffected = UserDA.insert(user)
    except Exception as e:
        print("-----insertUser-----")
        print(e)
        print("-----insertUser-----")
    return rowsAffected


def selectUser():
    users = []
    try:
        users = UserDA.select()
    except Exception as e:
        print("-----selectUser-----")
        print(e)
        print("-----selectUser-----")
    return users


def updateUser(user):
    rowsAffected = 0
    try:
        rowsAffected = UserDA.update(user)
    except Exception as e:
        print("-----updateUser-----")
        print(e)
        print("-----updateUser-----")
    return rowsAffected


def deleteUser(user):
    rowsAffected = 0
    try:
        rowsAffected = UserDA.delete(user)
    except Exception as e:
        print("-----deleteUser-----")
        print(e)
        print("-----deleteUser-----")
    return rowsAffected
