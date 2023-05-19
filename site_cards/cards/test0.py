import re
import requests
#, "5409979", "887851"
l_3, l_4 = [], []
company = ["3186887", "3558328"]

def pars_company(xx):
    request1 = "https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?size=200&atid=" + xx + "&cat=2075&cmp=1&sort=lst.d"
    request2 = "https://api.kufar.by/search-api/v1/search/rendered-paginated?size=100&atid=" + xx + "&cat=2075&cmp=1&sort=lst.d&cursor=eyJ0IjoiYWJzIiwiZiI6ZmFsc2UsInAiOjF9"
    request_list = [request1, request2]
    if xx == "3186887" or xx == "5409979":
        request_list = [request1]
    for aa in request_list:
        a = requests.get(aa)
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
    if len(request_list) > 1:
        l_3[0] = l_3[0] + l_3[1]
        for el in l_3[0]:
            count = 0
            for elem in l_3[0]:
                if elem[1] == el[1]:
                    count += 1
                    if count > 1:
                        del l_3[0][l_3[0].index(elem)]

        ss = 0
        for i in l_3[0]:
            ss += 1
            i[0] = ss
    #print(l_3)
    return l_3

#pars_company("887851")
for xx in company:
    pars_company(xx)
    l_4.append(l_3)
    print(l_3)





