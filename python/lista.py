import requests
from bs4 import BeautifulSoup

url = 'https://www.srednja.hr/srednja-kalkulator/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

b = soup.find()
print(b.text)