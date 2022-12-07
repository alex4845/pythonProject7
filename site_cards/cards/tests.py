import os

import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.kufar.by/user/3186887")
html = BS(r.content, 'html.parser')
c = html.select('.styles_wrapper__pb4qU')
list_1 = []
name_f = 0
for i in c:
    p = i.get("href")
    par = requests.get(p)
    html_1 = BS(par.content, 'html.parser')
    note = html_1.select('.styles_description_content__Lj7Ik')
    parameters = []
    for i in note:
        parameters.append(i.text)
    print(parameters)
    imgs = html_1.select('.styles_slide__image__lc2v_')

    for i in imgs:
        res = i.get("src")

        im = requests.get(res, stream=True).content
        print(res[49:59])
        if not os.path.exists('media/media/site_cards'):
            os.makedirs('media/media/site_cards')
        with open('media/media/site_cards/' + res[49:59] + '.jpg', "wb") as handler:
            handler.write(im)

    break
