from .helpers import get_mention
from .database import Database
from . import constants


def pidro(message, db: Database):
    mention_user_name = get_mention(message)
    if not mention_user_name:
        return constants.ERROR_USERNAME_NOT_FOUND
    pidro = db.add_pidro(message.chat.id, mention_user_name)
    answer = constants.ANSWER_ADD_PIDRO.format(username=mention_user_name, pidro=pidro)
    return answer


def stats(message, db: Database):
    df_statistic = db.get_stat(message.chat.id)
    answer = ''
    if df_statistic.empty:
        answer = constants.ERROR_EMPTY_STATS
    for n, row in df_statistic.iterrows():
        answer += constants.ANSWER_STATS.format(number=n+1, username=row['user_name'], rating=str(row['rating']))
    return answer
