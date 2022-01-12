from Model.DA import AnswerDA


def insertAnswer(answer, userId):
    rowsAffected = 0
    try:
        rowsAffected = AnswerDA.insert(answer, userId)
    except Exception as e:
        print("-----insertAnswer-----")
        print(e)
        print("-----insertAnswer-----")
    return rowsAffected


def selectAnswer():
    answers = []
    try:
        answers = AnswerDA.select()
    except Exception as e:
        print("-----selectAnswer-----")
        print(e)
        print("-----selectAnswer-----")
    return answers


def updateAnswer(answer, userId):
    rowsAffected = 0
    try:
        rowsAffected = AnswerDA.update(answer, userId)
    except Exception as e:
        print("-----updateAnswer-----")
        print(e)
        print("-----updateAnswer-----")
    return rowsAffected


def deleteAnswer(answer, userId):
    rowsAffected = 0
    try:
        rowsAffected = AnswerDA.delete(answer, userId)
    except Exception as e:
        print("-----deleteAnswer-----")
        print(e)
        print("-----deleteAnswer-----")
    return rowsAffected
