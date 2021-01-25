import os
from boto.s3.connection import S3Connection


TOKEN = S3Connection(os.environ.get('PIDROBOT_TOKEN'))

ANSWER_ADD_PIDRO = '{username} твой PIDRO-рейтинг {pidro}'
ANSWER_STATS = '{number}. {username} - {rating} \n'

ERROR_USERNAME_NOT_FOUND = 'В твоем сообщении мало смысла'
ERROR_EMPTY_STATS = 'Рейтинга нет'
