import re

import requests
from bs4 import BeautifulSoup, SoupStrainer

a = requests.get("https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?size=132&atid=3186887&cat=2075&cmp=1&sort=lst.d")


print(a.text)
# s = 0
# for i in re.findall('(https://[\S]+)', a.text):
#     s += 1
#     print(i[:34])
# print(s)
s, l_1 = 0, []
for i in re.findall('(subject":"....................................)', a.text):
    s += 1
    res, l_2 = "", []
    for y in i[10:]:
        if y == '"': break
        res = res + y
    l_2.append(s)
    l_2.append(res)
    l_1.append(l_2)

s = 0
for i in re.findall('(price_byn":"......)', a.text):
    res = ""
    for y in i[12:]:
        if y == '"': break
        res = res + y
    l_1[s].append(res[:-2] + " руб")
    s += 1

print(l_1)