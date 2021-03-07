from . import constants
import psycopg2


class Database:

    def __init__(self):
        self.conn = None
        self.connect()
        self.cur = self.conn.cursor()

    def add_pidro(self, username: str, chat_id: str):
        self.cur.execute(f"call public.add_rating('{username}', {chat_id});")
        self.conn.commit()

    def add_user(self, username, chat_id, chat_name):
        self.cur.execute(f"call public.add_user('{username}', {chat_id}, '{chat_name}');")
        self.conn.commit()

    def get_chat_stat(self, chat_id: str):
        result = []
        self.cur.execute(f"select u.username, u.rating, lu.chat_rating"
                         f" from public.users u, public.link_user_chat lu"
                         f" where u.username = lu.username"
                         f" and lu.chat_id = {chat_id}"
                         f" order by u.rating desc;")
        rows = self.cur.fetchall()
        for row in rows:
            user_stat = {'username': row[0], 'chat_rating': row[1], 'rating': row[2]}
            result.append(user_stat)
        return result

    def get_user_rating(self, username, chat_id):
        result = {}
        self.cur.execute(f"select u.rating, lu.chat_rating "
                         f"from public.users u, public.link_user_chat lu "
                         f"where u.username = '{username}' "
                         f"and lu.username = u.username "
                         f"and lu.chat_id = {chat_id}; ")
        rows = self.cur.fetchall()
        for row in rows:
            result = {'username': username, 'rating': row[0], 'chat_rating': row[1]}
        return result

    def connect(self):
        self.conn = psycopg2.connect(constants.DATABASE_URL, sslmode='require')

    def close(self):
        self.conn.close()
