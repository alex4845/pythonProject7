import re
import requests
import datetime
from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect

from cards.forms import ShineForm
from cards.models import Shine



def main_page(request):
    now = datetime.now()
    a = now.strftime("%H:%M:%S")
    # if a > "16:00:00":
    #     ubdate(request)

    return render(request, 'cards/index.html', {"a": a})

def report(request):
    if request.method == "GET":
        return render(request, 'cards/report.html')

    if request.method == "POST":
        saler = request.POST["saler"]
        if saler:
            if saler == "все":
                a = Shine.objects.all()
            else:
                a = Shine.objects.filter(
                    Q(company__iregex=saler) | Q(company__iregex=saler))
            b, byn_2, count = "", 0, 0
            count_B17 = 0
            for i in a:
                count += 1
                if int(i.number) == 1: b = str(i.company)
                elif "Б17" in i.short_note:
                    count_B17 += 1


                byn = i.price
                byn_1 = ""
                for el in str(byn):
                    if el.isdigit():
                        byn_1 = byn_1 + el
                    elif el == "р": break
                if byn_1 == "": by = 0
                else: by = int(byn_1)
                byn_2 = byn_2 + by
            if saler == "все": b = "всех продавцов"

            return render(request, 'cards/report.html',
                          {"b": b, "byn_2": byn_2, "count": count, "count_B17": count_B17})

def search(request):
     if request.method == "GET":
         return render(request, 'cards/search.html')

     if request.method == "POST":
         radius = request.POST["radius"]
         shirina = request.POST["shirina"]
         visota = request.POST["visota"]
         diametr = request.POST["diametr"]
         saler = request.POST["saler"]
         if radius and diametr:
             a = Shine.objects.filter(
                 Q(short_note__iregex=radius) | Q(short_note__iregex=radius)
             ).filter(short_note__contains=diametr)
         elif radius:
             a = Shine.objects.filter(
                 Q(short_note__iregex=radius) | Q(short_note__iregex=radius)
                 )
         elif shirina and visota:
             a = Shine.objects.filter(shirina__contains=shirina).filter(visota__contains=visota)
         elif shirina:
             a = Shine.objects.filter(shirina__contains=shirina)
         elif diametr:
             a = Shine.objects.filter(diametr__contains=diametr)
         elif saler:
             a = Shine.objects.filter(
                 Q(company__iregex=saler) | Q(company__iregex=saler)
                 )
         else:
             a = Shine.objects.all()

         b = "Шины с такими параметрами не обнаружены"
         return render(request, 'cards/search.html', {"a": a, "b": b, "radius": radius})


def del_card(request, pk):
    a = Shine.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'cards/action.html', {"a": a})


def ubdate(request):
    if request.method == "GET":
        a = Shine.objects.all()
        a.delete()#очистка бд
        #shutil.rmtree('media/media/site_cards')#удаление фоток

        l_3 = []
        company = ["3186887", "3558328", "5409979", "887851"]
        def pars_company(xx):
            request1 = "https://cre-api-v2.kufar.by/items-search/v1/engine/v1/search/rendered-paginated?size=200&atid=" + xx + "&cat=2075&cmp=1&sort=lst.d"
            request2 = "https://api.kufar.by/search-api/v1/search/rendered-paginated?size=100&atid=" + xx + "&cat=2075&cmp=1&sort=lst.d&cursor=eyJ0IjoiYWJzIiwiZiI6ZmFsc2UsInAiOjF9"
            request_list = [request1, request2]
            if xx == "3186887" or xx == "5409979":
                request_list = [request1]
            c = 0
            for aa in request_list:
                c += 1
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

                if c == 2:
                    l_3[-1] = l_3[-2] + l_1
                    for el in l_3[-1]:
                        count = 0
                        for elem in l_3[-1]:
                            if elem[1] == el[1]:
                                count += 1
                                if count > 1:
                                    del l_3[-1][l_3[-1].index(elem)]
                    del l_3[-2]
                    ss = 0
                    for i in l_3[-1]:
                        ss += 1
                        i[0] = ss

        for xx in company:
            pars_company(xx)

        r_count = 0
        for yy in l_3:

            for xx in yy:
                if yy == l_3[-1]:
                    xx[8] = "ЦентрТрансСнаб_2"
                a_1 = Shine(number=xx[0], href=xx[1], company=xx[8], shirina=xx[4], visota=xx[5],
                            diametr=xx[6], price=xx[3], short_note=xx[2])
                a_1.save()
                r_count += 1
        b_1 = 'Получны новые данные! '
        time = datetime.now()

        return render(request, 'cards/search.html',
                      {"b_1": b_1, "r_count": r_count, "time": time})
    if request.method == "POST":
        return redirect('search')


