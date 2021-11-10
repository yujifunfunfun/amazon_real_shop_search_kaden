import pandas as pd
import re


def load_model_number():
    df = pd.read_csv('Product_Finder.2021_11_7.products.csv',usecols=['Model'])
    df = df.fillna('None')
    df = df.values.tolist()
    model_number_list = []
    for model_number in df:
        model_number_list.append(model_number[0])

    return model_number_list

def load_buybox_asin():
    df = pd.read_csv('Product_Finder.2021_11_7.products.csv',usecols=['ASIN','Buy Box 🚚: 現在価格'])
    df = df.fillna('None')
    df = df.values.tolist()
    buybox_asin_list = []
    for buybox_asin in df:
        buybox = buybox_asin[0]
        buybox = re.sub(r'\D', '', buybox) 
        buybox_asin_list.append([buybox,buybox_asin[1]])
        
    return buybox_asin_list