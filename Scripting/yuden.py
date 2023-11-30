from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import csv

def import_data(path):
    try:
        df = pd.read_csv(path, dtype=str)
    except FileNotFoundError as error:
        from google.colab import drive
        drive.mount('/content/gdrive')

        df = pd.read_csv(path, dtype=str)

    return df

def export_data(df, path):
    df.to_csv(path)

def add_columns(columns):
    import numpy as np
  
    # check if the column already exists
    for column in columns:
        if not column in df.columns:
            df[column] = np.nan

def scrap_data():
  try:
    response = requests.get('https://ds.yuden.co.jp/TYCOMPAS/or/detail?pn=' + 'MSASP063EB5475MFNA01')
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find_all('table', attrs={'id': 'DetailTable'})
    td = table[0].find_all('td', attrs={'id': 'ProductSpecificationArea'})
    _table = td[0].find_all('table')
    _tr = _table[0].find_all('tr')
    item = {}
    for column in columns:
      if column == 'PartNumber':
        item[column] = 'MSASP063EB5475MFNA01'
      else:
        flg = False
        for _trItem in _tr:
          if _trItem.find_all('td', class_='ItemName')[0].text == column:
            flg = True
            item[column] = _trItem.find_all('td', class_='ItemValue')[0].text
        if flg == False:
          item[column] = 'null'
    return item
  except (IndexError, AttributeError, requests.exceptions.MissingSchema):
        print('part number is not found on server')
        return {"status":404}
  
# main run



path = '/content/drive/My Drive/yuden/yuden.csv'
df = import_data(path)
columns = ['PartNumber' ,'Status' ,'RoHS Compliance (10 subst.)' ,'REACH Compliance (233 subst.)' ,'Halogen Free' ,'RoHS Declarations' ,'REACH Declarations']
# add_columns(columns)
df.to_csv(path,index=False)

eachData = scrap_data()
print(eachData)
with open(path, mode='w', newline='') as file:
  fieldnames = columns
  writer = csv.DictWriter(file, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow(eachData)