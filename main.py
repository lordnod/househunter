#Goals:
#Scrape realtor sites for data on houses matching needs
#Use that data determine the cost and how long those houses are on the market
#Format data in an easily readable format from CSV (Probably using Google Sheets)
#?
#Profit!

from bs4 import BeautifulSoup
import requests, urlopen
import csv

desiredZip = 'insert desired zip code as an integer'
targetURL = 'make your search on realtor.com with your needs and put the search url here'

source = requests.get(targetURL).text

rawData = BeautifulSoup(source, 'lxml')
#rawPropData = rawData.find_all('li', class_='component_property-card js-component_property-card js-quick-view')

csv_file = open('house_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['streetAddress', 'city', 'state', 'zipCode', 'price'])

for house in rawData.find_all('li', class_='component_property-card js-component_property-card js-quick-view'):
    zipCode = house.find('span', itemprop='postalCode')
    zipCode = int(zipCode.text)
    if zipCode == desiredZip:
        streetAddress = house.find('span', itemprop='streetAddress')
        city = house.find('span', itemprop='addressLocality')
        state = house.find('span', itemprop='addressRegion')
        price = house.find('span', class_='data-price')
        csv_writer.writerow([streetAddress, city, state, price])
    
csv_file.close()

print('Done')
