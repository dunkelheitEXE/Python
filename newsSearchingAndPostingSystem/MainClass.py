from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'

SPREADSHEET_ID = '1ZhyiZBs68zz1AtSXT5qAwY4x39Kn0PUsuLwrgSWBWDo'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes = SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Llamada a la API
result = sheet.values().get(spreadsheetId = SPREADSHEET_ID, range = 'Hoja 1!A1:H1').execute()

# Extracción de valores
values = result.get('Values', [])
print(values)