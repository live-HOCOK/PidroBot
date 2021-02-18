from .helpers import get_mention
from .database import Database
from . import constants


def pidro(message, db: Database):
    mention_user_name = get_mention(message)
    if not mention_user_name:
        return constants.ERROR_USERNAME_NOT_FOUND
    db.add_user(mention_user_name, message.chat.id, message.chat.title)
    db.add_pidro(mention_user_name, message.chat.id)
    rating = db.get_user_rating(mention_user_name, message.chat.id)
    answer = constants.ANSWER_ADD_PIDRO.format(username=mention_user_name, rating=rating.get('chat_rating', 0))
    return answer


def stats(message, db: Database):
    statistic = db.get_chat_stat(message.chat.id)
    answer = ''
    if not statistic:
        answer = constants.ERROR_EMPTY_STATS
    n = 1
    for row in statistic:
        answer += constants.ANSWER_STATS.format(number=n, username=row['username'], rating=str(row['rating']))
        n += 1
    return answer
