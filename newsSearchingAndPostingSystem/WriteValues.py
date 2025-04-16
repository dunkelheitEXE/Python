from google.oauth2.credentials import Credentials 
from googleapiclient.discovery import build 
from google.oauth2 import service_account 

import requests
from bs4 import BeautifulSoup

import SearchingClass as sc

def sendByPortal():
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

    font_one = sc.SearchingClass(url='https://www.eleconomista.com.mx/buscar/?q=fintech', web="https://www.eleconomista.com.mx")

    to_send = font_one.get_data(
        articleTag='article',
        articleClass='c-article',
        headerTag='h3.c-article__title',
        pictureTag='picture img',
        descriptionTag='div.c-detail__body',
        authorTag='span.c-article__name',
        dateTag='time.c-article__date',
        insideLinkTag='h3.c-article__title a'
    )

    request = sheet.values().append(spreadsheetId = SPREADSHEET_ID, range='hoja 1', valueInputOption='USER_ENTERED', body={'values':to_send}).execute()
    print("Extracción y exportación FINALIZADAS exitosamente")