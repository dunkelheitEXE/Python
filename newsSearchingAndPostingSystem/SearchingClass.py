import requests
from bs4 import BeautifulSoup

class SearchingClass:
    url = None # URL del portal de noticias
    web = "" # En caso de que los recursos del portal
    # no sean accesibles directamente, y tengan un prefijo como
    # https://noticias/..., en esta variable se guardara ese
    # prefijo

    # Clase constructora
    def __init__ (self, url, web):
        self.url = url
        self.web = web
    
    # Esta es al funcion que recibe las etiquetas HTML y los selectores CSS
    # NO MODIFICAR
    def get_data(self, articleTag, articleClass, headerTag, pictureTag, descriptionTag, authorTag, dateTag, insideLinkTag):
        array = [] # se define la matriz por el cual se devolveran las noticias
        # con todas sus propiedades
        
        insideLinks = [] # Esta es una variable provisional, que sirve
        # para guardar los links que nos permitiran acceder al contenido 
        # de los articulos
        
        # Aqui se definen las variables que nos ayudaran a hacer
        # la busqueda a traves de la web en base a sus componentes
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Se define que etiqueta HTML y selector CSS define el contenedor de los articulos
        articles = soup.find_all(articleTag, class_ = articleClass)

        # Iteramos cada articulo
        # de cada iteración recuperaremos:
        # 1- Encabezado
        # 2- Foto
        # 3- Autor
        # 4- Fecha de publicacion
        # 5- thubnail de la foto
        # 6- Color del boton de lectura
        for article in articles:
            array.append([
                article.select_one(headerTag).text.strip(),
                article.select_one(pictureTag)['src'],
                article.select_one(authorTag).text.strip(),
                article.select_one(dateTag)['datetime'],
                article.select_one(pictureTag)['src'],
                '#d17a46'
            ])

            # Aqui se guardaran en la avriable provisional
            # los links de contenido, por el cual accederemos 
            # a los articulos completos
            insideLinks.append(self.web + article.select_one(insideLinkTag)['href'])

        # creamos un contador que nos ayudara
        # a avanzar en el arreglo de noticias ya 
        # guardadas en la matriz
        counter = 0
        
        # Creamos el ciclo que itera en cada link almacenado en la variable provisional
        for link in insideLinks:
            # Por cada link, necesitaremos las librerias
            # que nos permitan acceder a cada componente de CADA PAGINA WEB
            response_link = requests.get(link)
            soup_link = BeautifulSoup(response_link.text, 'html.parser')
            
            # Guardamos el contenido en base a la etiqueta HTML y
            # selectores CSS que tengan el texto completo de la nota
            # en la variable "content"
            content = soup_link.select_one(descriptionTag).text.strip()
            
            # Creamos la variable summary, que guardara el mismo texto
            # pero suprimido, este sera el texto que se muestre como preview
            summary = content[:100] + '...'
            
            # Lo insertamos en el arreglo de noticias, en la
            # posicion que le corresponde, en base a la hoja de calculo
            # de google sheets e iteramos en este arreglo gracias 
            # a counter
            array[counter].insert(2, content)
            array[counter].insert(5, summary)
            counter+=1
        
        # Al final retornamos la matriz con la información 
        # de cada nota del portal de noticias definido en la variable
        # "url"
        return array
