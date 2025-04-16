# Primeramente se importan las librerías 
# de google, estas librerías sirven para usar 
# Apis hechas en google cloud

# En este caso, la API es de Google sheets, usada, propieamente
# para acceder a una hoja de calculo siempre y cuando
# se le de acceso a través de la propia hoja
# al correo ligado a esta API
from google.oauth2.credentials import Credentials 
from googleapiclient.discovery import build 
from google.oauth2 import service_account 

# Librerías para hacer web scraping
import requests
from bs4 import BeautifulSoup

import SearchingClass as sc

# Se define la función que mandará a la hoja de calculo la información necesaría
def sendByPortal():
    
    # defninimos el scope usando la API de google sheets
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] 
    
    # definimos la KEY, esta KEY nos dará acceso a la API
    # y a la cuenta que va a interactuar con la hoja de calculo
    KEY = 'key.json' 
    
    # Defninimos el ID de la hoja de calculo
    SPREADSHEET_ID = '1ZhyiZBs68zz1AtSXT5qAwY4x39Kn0PUsuLwrgSWBWDo' 

    # Definimos la variable que guardara las credenciales
    # de la revice account usada como API
    creds = None
    creds = service_account.Credentials.from_service_account_file(KEY, scopes = SCOPES) 

    # Definimos la configuración de la hoja
    service = build('sheets', 'v4', credentials=creds) 
    sheet = service.spreadsheets() 
    # Aqui se define que hoja es en la que se escribira informacion
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="Hoja 1").execute()

    #Debe ser una matriz por eso el doble [[]] 
    # Aqui se guardaran los valores a escribir
    values = result.get('values', [])

    # Aqui se definen los valores de la clase de busqueda
    # de noticias y web scraping
    font_one = sc.SearchingClass(url='https://www.eleconomista.com.mx/buscar/?q=fintech', web="https://www.eleconomista.com.mx")

    # En esta funcion se estan definiendo las etiquetas y selectores CSS
    # por los caules se tomarán las noticias (NO MODIFICAR!) 
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

    # Se hace la peticion de impresion en la hoja de calculo
    request = sheet.values().append(spreadsheetId = SPREADSHEET_ID, range='hoja 1', valueInputOption='USER_ENTERED', body={'values':to_send}).execute()
    # Se muestra mensaje de confirmación
    print("Extracción y exportación FINALIZADAS exitosamente")