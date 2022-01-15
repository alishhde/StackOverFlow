from Server.Model.DA import CommentDA


def insertComment(comment, userId):
    rowsAffected = 0
    try:
        rowsAffected = CommentDA.insert(comment, userId)
    except Exception as e:
        print("-----insertComment-----")
        print(e)
        print("-----insertComment-----")
    return rowsAffected


def selectComment():
    comments = []
    try:
        comments = CommentDA.select()
    except Exception as e:
        print("-----selectComment-----")
        print(e)
        print("-----selectComment-----")
    return comments


def updateComment(comment, userId):
    rowsAffected = 0
    try:
        rowsAffected = CommentDA.update(comment, userId)
    except Exception as e:
        print("-----updateComment-----")
        print(e)
        print("-----updateComment-----")
    return rowsAffected


def deleteComment(comment, userId):
    rowsAffected = 0
    try:
        rowsAffected = CommentDA.delete(comment, userId)
    except Exception as e:
        print("-----deleteComment-----")
        print(e)
        print("-----deleteComment-----")
    return rowsAffected
