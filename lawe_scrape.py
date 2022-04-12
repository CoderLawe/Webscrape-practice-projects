from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://lawe.pythonanywhere.com').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cartopia_scrape.csv','w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Title','Written BY', 'Image Links'])
#print(soup.prettify())

for card in soup.find_all('div',class_='card'):

    #body = card.find('div', class_='card-body')
    title = card.find('div', class_='card-title').p.text
    print(title)

    author = card.find('p', class_='text-muted').text

    author = author.split(' ')

    author = author[3]
    print(author)

    image_src = card.find('img')['src']
    image_src = image_src.split('/')

    image_link = image_src[3]

    image_link = f'https://lawe.pythonanywhere.com/media/images/{image_link}'
    #print(image_src)
    print(image_link)
    #print(image_src)

    #https://lawe.pythonanywhere.com/media/images/ford-2705402_1920.jpg

    csv_writer.writerow([title,author, image_link])

csv_file.close()