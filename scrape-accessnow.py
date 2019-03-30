from bs4 import BeautifulSoup
import io

htmldoc = open ("AccessNow.html", "r")

soup = BeautifulSoup(htmldoc, 'lxml')

googleDestinations = []

for link in soup.find_all('a'):
    googleDestinations.append(link.get('href'))

googleDestinations = googleDestinations [5:]

import pandas as pd

df = pd.DataFrame(googleDestinations)

df.head()
