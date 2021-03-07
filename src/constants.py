import os


TOKEN = os.environ.get('PIDROBOT_TOKEN')
DATABASE_URL = os.environ.get('DATABASE_URL')

ANSWER_ADD_PIDRO = '{username} твой PIDRO-рейтинг в чате - {rating}'
ANSWER_STATS = '{number}. {username} - рейтинг в чате {rating}, глобальный рейтинг {global_rating} \n'

ERROR_USERNAME_NOT_FOUND = 'В твоем сообщении мало смысла'
ERROR_EMPTY_STATS = 'Рейтинга нет'


SYNONYMS_PIDRO_COMMAND = ['пидр', 'пидор', 'гандон', 'гондон', 'пидорюга', 'гей', 'ты пидор', 'ты пидр']
