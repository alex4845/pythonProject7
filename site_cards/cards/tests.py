import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.kufar.by/user/3186887")
html = BS(r.content, 'html.parser')
c = html.select('.styles_wrapper__pb4qU')
for i in c:
    print(i.text)



