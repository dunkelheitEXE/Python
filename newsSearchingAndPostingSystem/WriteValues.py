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

to_send = sc.devol()

request = sheet.values().append(spreadsheetId = SPREADSHEET_ID, range='hoja 1', valueInputOption='USER_ENTERED', body={'values':to_send}).execute()
print("Finalizado")