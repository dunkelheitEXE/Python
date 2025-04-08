import requests
from bs4 import BeautifulSoup



def devol():
    url = 'https://www.eleconomista.com.mx/buscar/?q=fintech'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Header	
    # Picture
    # Description	
    # Author	
    # Date	
    # Post Sumary	
    # Thumbnail image	
    # Color
    tags = {
        'header': 'h3.c-article__title',
        'picture': 'picture img',
        'description': 'div.c-detail__body',
        'author': 'span.c-article__name',
        'date': 'time.c-article__date',
        'post_summary': 'div.c-detail__body',
        'thumbnail_image': 'picture img',
        'color': '#d07e56',
        'articleLink': 'h3.c-article__title a'
    }

    articles = soup.find_all('article', class_='c-article')
    array = []
    links = []
    website = 'https://www.eleconomista.com.mx'

    for i in range(len(articles)):
        array.append([
            articles[i].select_one(tags['header']).text.strip(),
            articles[i].select_one(tags['picture'])['src'],
            articles[i].select_one(tags['author']).text.strip(),
            articles[i].select_one(tags['date'])['datetime'],
            articles[i].select_one(tags['thumbnail_image'])['src'],
            tags['color'],
        ])


        links.append(website + articles[i].select_one(tags['articleLink'])['href'])

    for i in range(len(array)):
        response_link = requests.get(links[i])
        soup_link = BeautifulSoup(response_link.text, 'html.parser')

        content = soup_link.select_one(tags['description']).text.strip()
        array[i].insert(2, content)
        array[i].insert(5, content[:100] + "...")
    
    return array

