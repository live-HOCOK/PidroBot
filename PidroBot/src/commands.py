from .helpers import get_mention
from .database import Database
from . import constants


def pidro(message, db: Database):
    mention_user_name = get_mention(message)
    if not mention_user_name:
        return constants.ERROR_USERNAME_NOT_FOUND
    pidro = 0
    answer = constants.ANSWER_ADD_PIDRO.format(username=mention_user_name, pidro=pidro)
    return answer


def stats(message, db):
    pass
