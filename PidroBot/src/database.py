import pandas as pd


class Database:

    def __init__(self):
        self.df = pd.DataFrame(columns=['chat_id', 'user_name', 'rating'])

    def add_pidro(self, chat_id: str, user_name: str):
        pass

    def get_pidro(self, chat_id: str, user_name: str):
        pass
