import os

import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.kufar.by/user/3186887")
html = BS(r.content, 'html.parser')
c = html.select('.styles_tabs__content__HyzDW.styles_pro-page__tabs-content__fWmnz')
x = 0
for i in c:
    #p = i.get("href")
    x +=1
    print(i.text)
print(x)



exit(0)
    # par = requests.get(p)
    # html_1 = BS(par.content, 'html.parser')
    # note = html_1.select('.styles_description_content__Lj7Ik')
    # parameters = []
    # for i in note:
    #     parameters.append(i.text)

page = html.select('.styles_link__p7Uwk')
for i in page:
    res = i.get("href")
    if res == None:
        continue

    res_1 = requests.get(f"https://www.kufar.by{res}")
    html_2 = BS(res_1.content, 'html.parser')
    res_2 = html_2.select('.styles_title__wj__Y')
    for el in res_2:
        print(el.text)


    #print(f"https://www.kufar.by{res}")



