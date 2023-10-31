from bs4 import BeautifulSoup
import requests


url = "https://yandex.com.am/weather/?lat=44.72377014&lon=37.76881409"
response = requests.get(url)

bs = BeautifulSoup(response.text, "lxml")


temp = bs.find('span', 'temp__value temp__value_with-unit')
print(temp)
