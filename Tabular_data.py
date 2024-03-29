import pandas as pd
import matplotlib as plt
import numpy as np
import string
from Load_dataset import download_ziplink

class TabularData_C():
    def __init__(self) -> None:
        self.df= None
        self.id_list= None
        self.row_nums= None
        
    def read_file(self,file_dir):
        file_directory = file_dir
        self.df = pd.read_csv(file_directory)

    def get_num_rows(self):
        self.row_nums = len(self.df.index)

    def make_alphabetical_list(self)-> list:
        alphabet = string.ascii_uppercase
        index_list = []
        for first in alphabet:
            for second in alphabet:
                for third in alphabet:
                    index_list.append(first + second + third)
        matched_list = index_list[:self.row_nums]
        self.id_list = matched_list

    def reannotate_id(self):
        self.df["ID"] = self.id_list
        self.df.set_index("ID", inplace=True)
        self.df.to_csv('data.csv',index=False)
        self.df = pd.read_csv('data.csv')


    def remove_rows_with_missing_ratings(self):
            #removes rows that have missing values in the columns containing 'rating' in their names
        self.df = self.df.dropna(subset = ['Cleanliness_rating','Accuracy_rating','Communication_rating','Location_rating','Check-in_rating','Value_rating'])
        self.df.to_csv('rows_missing_ratings_removed.csv',index=False)
        self.df = pd.read_csv('rows_missing_ratings_removed.csv')

    def combine_description_strings(self):
            #Description column is being turned into string, 'About this space' is dropped, some symbols are dropped as well.
        
        # self.df['Description'] = self.df['Description'].apply(lambda x: ast.literal_eval(x))
        self.df= pd.read_csv('rows_missing_ratings_removed.csv')
        self.df=self.df[self.df['Description'].str.contains('About this space')== True]
        # self.df['Description'] = self.df[self.df['Description'].str.startswith('About this space', na= False)]
        self.df['Description'] = self.df['Description'].str.replace("'About this space',","")
        self.df['Description'] = self.df['Description'].str.replace('"',"")
        self.df['Description'] = self.df['Description'].str.replace("' '","")
        self.df['Description'] = self.df['Description'].str.replace("'","")
        self.df= self.df.dropna(subset=['Description'])
        self.df.to_csv('descriptions_joined.csv',index=False)
        self.df = pd.read_csv('descriptions_joined.csv')
    
    def set_default_feature_values(self):
            #updates rows that have missing values in the columns guests, beds, bathrooms, bedrooms by replacing NaN with 1.
        self.df = pd.read_csv('descriptions_joined.csv')
        self.df.loc[self.df['guests'].isnull(),['guests']] = 1 
        self.df.loc[self.df['beds'].isnull(),['beds']] = 1  
        self.df.loc[self.df['bathrooms'].isnull(),['bathrooms']] = 1  
        self.df.loc[self.df['bedrooms'].isnull(),['bedrooms']] = 1 
        self.df.to_csv('blank cells filled to 1.csv',index=False)
        self.df = pd.read_csv('blank cells filled to 1.csv')

            # col_list=["guests", "beds", "bathrooms", "bedrooms"]
            # self.df[col_list] = df[col_list].fillna(1)

    def save_data_as_cleaned_dataframe(self):
        self.df.to_csv('clean_tabular_data.csv',index=True)
        self.df.info()
        print(self.df.isnull().sum())   # checks for any remaining empty cells.

    def load_airbnb(self,cleaned_dataset):
        dataset = pd.read_csv(cleaned_dataset)
        features = dataset[["guests","beds","bathrooms","Cleanliness_rating","Accuracy_rating","Communication_rating","Location_rating","Check-in_rating","Value_rating","amenities_count"]]
        labels = dataset[["Price_Night"]]
        loaded_data = features,labels
        return loaded_data
