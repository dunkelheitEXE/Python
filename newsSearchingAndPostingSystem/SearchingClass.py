import requests
from bs4 import BeautifulSoup

class SearchingClass:
    url = None
    web = ""

    def __init__ (self, url, web):
        self.url = url
        self.web = web
    
    def get_data(self, articleTag, articleClass, headerTag, pictureTag, descriptionTag, authorTag, dateTag, insideLinkTag):
        array = []
        insideLinks = []
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.find_all(articleTag, class_ = articleClass)

        for article in articles:
            array.append([
                article.select_one(headerTag).text.strip(),
                article.select_one(pictureTag)['src'],
                article.select_one(authorTag).text.strip(),
                article.select_one(dateTag)['datetime'],
                article.select_one(pictureTag)['src'],
                '#d17a46'
            ])

            insideLinks.append(self.web + article.select_one(insideLinkTag)['href'])

        counter = 0
        for link in insideLinks:
            response_link = requests.get(link)
            soup_link = BeautifulSoup(response_link.text, 'html.parser')
            
            content = soup_link.select_one(descriptionTag).text.strip()
            summary = content[:100] + '...'
            
            array[counter].insert(2, content)
            array[counter].insert(5, summary)
            counter+=1
        return array
            
            

# def devol():
#     url = 'https://www.eleconomista.com.mx/buscar/?q=fintech'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # Header	
#     # Picture
#     # Description	
#     # Author	
#     # Date	
#     # Post Sumary	
#     # Thumbnail image	
#     # Color
#     tags = {
#         'header': 'h3.c-article__title',
#         'picture': 'picture img',
#         'description': 'div.c-detail__body',
#         'author': 'span.c-article__name',
#         'date': 'time.c-article__date',
#         'post_summary': 'div.c-detail__body',
#         'thumbnail_image': 'picture img',
#         'color': '#d07e56',
#         'articleLink': 'h3.c-article__title a'
#     }

#     articles = soup.find_all('article', class_='c-article')
#     array = []
#     links = []
#     website = 'https://www.eleconomista.com.mx'

#     for i in range(len(articles)):
#         array.append([
#             articles[i].select_one(tags['header']).text.strip(),
#             articles[i].select_one(tags['picture'])['src'],
#             articles[i].select_one(tags['author']).text.strip(),
#             articles[i].select_one(tags['date'])['datetime'],
#             articles[i].select_one(tags['thumbnail_image'])['src'],
#             tags['color'],
#         ])


#         links.append(website + articles[i].select_one(tags['articleLink'])['href'])

#     for i in range(len(array)):
#         response_link = requests.get(links[i])
#         soup_link = BeautifulSoup(response_link.text, 'html.parser')

#         content = soup_link.select_one(tags['description']).text.strip()
#         array[i].insert(2, content)
#         array[i].insert(5, content[:100] + "...")
    
#     return array

