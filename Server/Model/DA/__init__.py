from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///D:\\My Works\\Projects\\Python Projects\\Project StackOverFlow\\Stackoverflow\\Server\\StackOverflowDB.db', echo=True)
Base = declarative_base()
Session = sessionmaker(engine)
session = Session()


def object_as_dict(obj):
    result = {instance.key: getattr(obj, instance.key) for instance in inspect(obj).mapper.column_attrs}
    try:
        if obj.questions[0].id:
            questions = []
            for question in obj.questions:
                question = {instance.key: getattr(question, instance.key) for instance in
                            inspect(question).mapper.column_attrs}
                questions.append(question)
            result["questions"] = questions
    except Exception as e:
        print(e)
    try:
        if obj.answers[0].id:
            answers = []
            for answer in obj.answers:
                answer = {instance.key: getattr(answer, instance.key) for instance in
                          inspect(answer).mapper.column_attrs}
                answers.append(answer)
            result["answers"] = answers
    except Exception as e:
        print(e)
    return result
