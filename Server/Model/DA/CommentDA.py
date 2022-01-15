from Server.Config.SqlalchemyUtils import session
from Server.Model.TO.Comment import Comment
from Server.Model.TO.User import User


def insert(comment, userId):
    session.add(comment)
    user = session.query(User).filter(userId)
    user.comments.append(comment)
    session.commit()
    return 1


def select():
    comments = session.query(Comment).all()
    session.commit()
    return comments


def update(comment, userId):
    session.query(Comment).filter(comment.id).update(
        {Comment.id: comment.id, Comment.body: comment.body, Comment.voteCount: comment.voteCount,
         Comment.userId: comment.userId, Comment.questionId: comment.questionId, Comment.answerId: comment.answerId},
        synchronize_session=False)
    comments = session.query(User).filter(userId).comments
    for commenti in comments:
        if commenti.id == comment.id:
            comments[commenti.index()] = comment
    session.commit()
    return 1


def delete(comment, userId):
    session.query(Comment).filter(comment.id).delete()
    user = session.query(User).filter(userId)
    user.comments.remove(comment)
    session.commit()
    return 1
