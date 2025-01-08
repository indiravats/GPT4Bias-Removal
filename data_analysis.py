import pandas as pd
import re

class DataAnlaysis():
    def __init__(self):
        self.df = None
    def remove_urls(self, text):
        url_pattern = r'http\S+|www\S+'
        return re.sub(url_pattern, '', text)

    def read_data(self):
        self.df = pd.read_csv('data/India_subreddit_comments.csv')[0:10]
    def get_dict_string_threadId(self):
        dataframe_comment_thread = self.df[['body','thread_id']]
        # print(self.df.head())
        # print(dataframe_comment_thread[0:5].to_dict('dict'))
        return dataframe_comment_thread
    def clean_text(self):
        self.read_data()
        self.get_dict_string_threadId()
        self.df['body'] = self.df['body'].apply(lambda x: self.remove_urls(x))
        print(self.df.head())


da = DataAnlaysis()
df_comment = da.clean_text()