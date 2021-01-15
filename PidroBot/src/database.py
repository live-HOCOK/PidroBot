import pandas as pd


class Database:

    def __init__(self):
        self.df = pd.DataFrame(columns=['chat_id', 'user_name', 'rating'])

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
        return result
