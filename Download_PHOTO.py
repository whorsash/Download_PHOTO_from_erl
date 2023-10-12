from tkinter import Tk

import tkinter.filedialog as fd

from io import BytesIO

import pandas as pd

import wget

import urllib.request
import urllib.error

import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

Tk().withdraw()
print('Выберите файл Excel')
filename = fd.askopenfilename()
if filename == '':
    print('Не выбран файл EXCEL')

print('Выберите путь для сохранения фото')
directory = fd.askdirectory()
if directory == '':
    print('Не выбран путь для сохранения фото')

url_text = input('Введите путь ссылки: ')

def download(SKU):
    url = url_text + SKU + '.jpg'
    check = requests.head(url)
    # print(check.status_code)
    if check.status_code == 200:
        #wget.download(url, directory + '/' + SKU + '.jpg')
        urllib.request.urlretrieve(url, directory + '/' + SKU + '.jpg')
    # else:
    #     try:
    #         urllib.request.urlretrieve(url)
    #     except urllib.error.HTTPError as err:
    #         print(url, err.code)
    #     else:
    #         wget.download(url, directory + '/' + SKU + '.jpg')
    #         # urllib.request.urlretrieve(url, directory + '/' + str(SKU) + '.jpg')


excel_data_df = pd.read_excel(filename)

rv = BytesIO()
count = 0
for df in excel_data_df['SKU'].tolist():
    count += 1
    text = ''
    print('№', str(count) + ', SKU:', df)
    download(str(df))
    text = ''
    for i in range(0, 16):
        text = str(df) + '_' + str(i)
        download(text)

i = input("Press Enter to continue: ")
print('Готово!')
