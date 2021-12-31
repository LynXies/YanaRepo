import requests
from bs4 import BeautifulSoup as BS
import sqlite3
import DbContext
import json

def save(slovar):
    with open('tsitata.txt', 'a') as file:
        file.write(f"{slovar['quotes']} -> Author:{slovar['authors']} -> Link:{slovar['link']} \n")
def parseQotes():
    allSlovars = []
    i = 1
    while True:
        URL = f'https://quotes.toscrape.com/page/{i}'
        i += 1
    
        response = requests.get(URL)

        # проверка на статус ответа сервера
        if response.status_code != 200:
            break

        soup = BS(response.content, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        # quotes = soup.findAll('div', class_='quote')[:1]

        if len(quotes) < 1:
            break

        slovars = []


        for quote in quotes:
            slovars.append({
                'quotes': quote.find('span', class_='text').get_text(strip=True),
                'authors': quote.find('small', class_='author').get_text(strip=True),
                'link': quote.find('a', href=True).get('href')

                
            })
            
        for slovar in slovars:
            print(f"page{i - 1} {slovar['quotes']} -> Author:{slovar['authors']} -> Link:{slovar['link']}")
           
        allSlovars += slovars

    return allSlovars

#parseQotes()

#создание схемы данных
context = DbContext.DbContext("parserDbTest2.db")


context.CreateTable("collection_of_quotes", (('quotes', 'TEXT', ('PRIMARY KEY', 'NOT NULL',)),
                                            ('authors', 'TEXT', ('NOT NULL',)),
                                            ('link', 'TEXT', ('NOT NULL'))))

data = parseQotes()
print(f"{len(data)} read")

values = [(d['quotes'], d['authors'], d['link']) for d in data]
columns = ('quotes', 'authors', 'link')
#Привод данных к заполнению
for v in values:
    context.Insert("collection_of_quotes", columns, v)

context.Disconnect()
