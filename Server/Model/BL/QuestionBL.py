from Server.Model.DA import QuestionDA


def insertQuestion(question, userId):
    rowsAffected = 0
    try:
        rowsAffected = QuestionDA.insert(question, userId)
    except Exception as e:
        print("-----insertQuestion-----")
        print(e)
        print("-----insertQuestion-----")
    return rowsAffected


def selectQuestion():
    questions = []
    try:
        questions = QuestionDA.select()
    except Exception as e:
        print("-----selectQuestion-----")
        print(e)
        print("-----selectQuestion-----")
    return questions


def updateQuestion(question, userId):
    rowsAffected = 0
    try:
        rowsAffected = QuestionDA.update(question, userId)
    except Exception as e:
        print("-----updateQuestion-----")
        print(e)
        print("-----updateQuestion-----")
    return rowsAffected


def deleteQuestion(question, userId):
    rowsAffected = 0
    try:
        rowsAffected = QuestionDA.delete(question, userId)
    except Exception as e:
        print("-----deleteQuestion-----")
        print(e)
        print("-----deleteQuestion-----")
    return rowsAffected
