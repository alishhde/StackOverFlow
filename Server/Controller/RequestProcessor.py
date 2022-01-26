import json

from Server.Model.BL.AnswerBL import insertAnswer, selectAnswer, updateAnswer, deleteAnswer
from Server.Model.BL.QuestionBL import insertQuestion, selectQuestion, updateQuestion, deleteQuestion
from Server.Model.BL.UserBL import insertUser, selectUser, updateUser, deleteUser, verifyUser
from Server.Model.TO import User


def processRequest(request):
    response = None
    if request[0] == 'AnswerBL':
        response = processAnswerRequest(request[1:])
    elif request[0] == 'QuestionBL':
        response = processQuestionRequest(request[1:])
    elif request[0] == 'UserBL':
        response = processUserRequest(request[1:])
    return "{}".format(response)


def processAnswerRequest(request):
    response = None
    if request[0] == 'insertAnswer':
        response = insertAnswer(request[1], request[2])
    elif request[0] == 'selectAnswer':
        response = selectAnswer()
    elif request[0] == 'updateAnswer':
        response = updateAnswer(request[1], request[2])
    elif request[0] == 'deleteAnswer':
        response = deleteAnswer(request[1], request[2])
    return response


def processQuestionRequest(request):
    response = None
    if request[0] == 'insertQuestion':
        response = insertQuestion(request[1], request[2])
    elif request[0] == 'selectQuestion':
        response = selectQuestion()
    elif request[0] == 'updateQuestion':
        response = updateQuestion(request[1], request[2])
    elif request[0] == 'deleteQuestion':
        response = deleteQuestion(request[1], request[2])
    return response


def processUserRequest(request):
    response = None
    if request[0] == 'verifyUser':
        response = verifyUser(request[1], request[2])
    elif request[0] == 'insertUser':
        j = json.loads(request[1])
        user = User(**j)
        response = insertUser(user)
    elif request[0] == 'selectUser':
        response = selectUser(request[1])
    elif request[0] == 'updateUser':
        response = updateUser(request[1])
    elif request[0] == 'deleteUser':
        response = deleteUser(request[1])
    return response
