from .database import Database
from . import constants


def get_mention(message):
    if not message.entities:
        return None
    for entity in message.entities:
        if entity.type == 'mention':
            start_position = message.text.find('@')
            mention = message.text[start_position:start_position + entity.length]
            return mention
    return None


def add_rating(mention_username, message, db: Database):
    db.add_user(mention_username, message.chat.id, message.chat.title)
    db.add_pidro(mention_username, message.chat.id)
    rating = db.get_user_rating(mention_username, message.chat.id)
    answer = constants.ANSWER_ADD_PIDRO.format(username=mention_username, rating=rating.get('chat_rating', 0))
    return answer
