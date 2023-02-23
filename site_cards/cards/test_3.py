import re
import requests


l_3 = []
company = ["3186887", "3558328", "5409979", "2938958", "",  "2938958(2)"]
for xx in company:
   if xx == company[-2]:
      a = requests.get(
         "https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?size=200&atid=2938958&cat=2075&cmp=1&sort=lst.d&cursor=eyJ0IjoicmVsIiwiYyI6W3sibiI6Imxpc3RfdGltZSIsInYiOjE2NzU2NTQ5NjUwMDB9LHsibiI6ImFkX2lkIiwidiI6MTcyNzQwMDIxfV0sImYiOnRydWV9")
   elif xx == company[-1]:
      a = requests.get("https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?size=300&atid=2938958&cat=2075&cmp=1&sort=lst.d&cursor=eyJ0IjoiYWJzIiwiZiI6ZmFsc2UsInAiOjF9")
   else:
      a = requests.get(
         "https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?size=300&atid=" + xx + "&cat=2075&cmp=1&sort=lst.d")

   s, l_1 = 0, []
   param = ['(,"subject":"..........................................................)',
            '(price_byn":"......)', '(рина","vl":"...)', '(сота","vl":"...)',
            '(метр","vl":"...)', '(езон","vl":".............)', '("name","v":".......................)']

   for i in re.split("auto.kufar", a.text):
      l_2 = []
      for y in range(0, len(param)):
         aa = str(re.findall(param[y], i))
         res = ""
         for x in aa[14:]:
            if x == '"' or x == "'":
               break
            res = res + x
         if y == 1: res = res[:-2]
         l_2.append(res)
      l_2.insert(0, "https://auto.kufar" + i[:16])
      l_2.insert(0, s)
      s += 1
      l_1.append(l_2)
      if l_1[-1][-1] == "":
         l_1[-1][-1] = l_1[-2][-1]

   del l_1[0]
   l_3.append(l_1)

l_3[3] = l_3[3] + l_3[4] + l_3[5]
del l_3[4:]
for el in l_3[3]:
   count = 0
   for elem in l_3[3]:

      if elem[1] == el[1]:
         count += 1
         if count > 1:
            del l_3[3][l_3[3].index(elem)]
ss = 0
for i in l_3[3]:
   ss += 1
   i[0] = ss

for yy in l_3:
   for xx in yy:
      print(xx)




