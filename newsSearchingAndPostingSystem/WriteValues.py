from google.oauth2.credentials import Credentials 
from googleapiclient.discovery import build 
from google.oauth2 import service_account 

import requests
from bs4 import BeautifulSoup


import SearchingClass as sc

SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] 
KEY = 'key.json' 
SPREADSHEET_ID = '1ZhyiZBs68zz1AtSXT5qAwY4x39Kn0PUsuLwrgSWBWDo' 

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes = SCOPES) 

service = build('sheets', 'v4', credentials=creds) 
sheet = service.spreadsheets() 
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="Hoja 1").execute()

#Debe ser una matriz por eso el doble [[]] 
values = result.get('values', [])

font_one = sc.SearchingClass(url='https://elpais.com/noticias/tecnologia-financiera/', web="")

to_send = font_one.get_data(
    articleTag='article',
    articleClass='c',
    headerTag='header.c_h',
    pictureTag='article img',
    descriptionTag='div.a_c.clearfix',
    authorTag='div.c_a',
    dateTag='div.c_a span.c_a_t time',
    insideLinkTag='h2.c_t a'
)

request = sheet.values().append(spreadsheetId = SPREADSHEET_ID, range='hoja 1', valueInputOption='USER_ENTERED', body={'values':to_send}).execute()
print("Finalizado")