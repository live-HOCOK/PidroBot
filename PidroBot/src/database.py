import pandas as pd
import os


class Database:

    def __init__(self):
        self.df = pd.DataFrame(columns=['chat_id', 'user_name', 'rating'])
        self.open_db()

    def add_pidro(self, chat_id: str, user_name: str):
        if self.df[(self.df.chat_id == chat_id) & (self.df.user_name == user_name)].empty:
            self.df.loc[len(self.df)] = [chat_id, user_name, 0]
        self.df.loc[(self.df['chat_id'] == chat_id) & (self.df['user_name'] == user_name), 'rating'] += 1
        rating = self.df[(self.df.chat_id == chat_id) & (self.df.user_name == user_name)].rating
        return rating.loc[rating.index[0]]

    def get_stat(self, chat_id: str):
        result = pd.DataFrame()
        if self.df[self.df.chat_id == chat_id].empty:
            return result
        result = self.df[self.df.chat_id == chat_id]
        self.order_df()
        self.save_db()
        return result

    def save_db(self):
        if not os.path.exists('./data'):
            os.mkdir('./data')
        self.df.to_csv('./data/db.csv', index=False, sep=';', encoding='utf-8-sig')

    def open_db(self):
        if os.path.exists('./data') and os.path.isfile('./data/db.csv'):
            self.df = pd.read_csv('./data/db.csv', sep=';')

    def order_df(self):
        self.df = self.df.sort_values(['rating', 'user_name'], ascending=True)
        self.df.reset_index(drop=True)
