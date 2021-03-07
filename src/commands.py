from .helpers import get_mention, add_rating
from .database import Database
from . import constants


def pidro(message, db: Database):
    mention_user_name = get_mention(message)
    if not mention_user_name:
        return constants.ERROR_USERNAME_NOT_FOUND
    return add_rating(mention_user_name, message, db)


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


def answer_all_mentions(message, db: Database):
    mention_user_name = get_mention(message)
    if not mention_user_name:
        return None
    parsed_text = message.text.replace(f'{mention_user_name} ', '')
    for synonym in constants.SYNONYMS_PIDRO_COMMAND:
        if parsed_text.lower() == synonym:
            return add_rating(mention_user_name, message, db)
