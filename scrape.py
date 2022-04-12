from bs4 import BeautifulSoup
import requests
import lxml

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):

    headline = article.h2.a.text
    print('Title', headline)

    summary = article.find('div', class_='entry-content').p.text
    print('Summary',summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']


        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    print('link',yt_link)

    print() 
    