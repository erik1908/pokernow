from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.pokernow.club/games/NphcJvfT86oytxGdK645wXB9J"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup)