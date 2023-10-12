import re
import requests
import datetime
from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect

from cards.forms import ShineForm
from cards.models import Shine, Times


def main_page(request):
    now = datetime.now()
    a = now.strftime('%d-%m-%Y %H:%M')
    tims = Times.objects.all()

    return render(request, 'cards/index.html', {"a": a, "tims": tims})

# def report(request):
#     if request.method == "GET":
#         return render(request, 'cards/report.html')
#
#     if request.method == "POST":
#         saler = request.POST["saler"]
#         if saler:
#             if saler == "все":
#                 a = Shine.objects.all()
#             else:
#                 a = Shine.objects.filter(
#                     Q(company__iregex=saler) | Q(company__iregex=saler))
#             b, byn_2, count = "", 0, 0
#             count_B17 = 0
#             for i in a:
#                 count += 1
#                 if int(i.number) == 1: b = str(i.company)
#                 elif "Б17" in i.short_note:
#                     count_B17 += 1
#
#                 byn = i.price
#                 byn_1 = ""
#                 for el in str(byn):
#                     if el.isdigit():
#                         byn_1 = byn_1 + el
#                     elif el == "р": break
#                 if byn_1 == "": by = 0
#                 else: by = int(byn_1)
#                 byn_2 = byn_2 + by
#             if saler == "все": b = "всех продавцов"
#
#             return render(request, 'cards/report.html',
#                           {"b": b, "byn_2": byn_2, "count": count, "count_B17": count_B17})

def search(request):
     tims = Times.objects.all()
     if request.method == "GET":
         return render(request, 'cards/search.html', {"tims": tims})

     if request.method == "POST":
         radius = request.POST["radius"]
         shirina = request.POST["shirina"]
         visota = request.POST["visota"]
         diametr = request.POST["diametr"]
         saler = request.POST["saler"]
         if radius and diametr:
             a = Shine.objects.filter(
                 Q(short_note__iregex=radius) | Q(short_note__iregex=radius)
             ).filter(diametr_d__contains=diametr)
         elif radius:
             a = Shine.objects.filter(
                 Q(short_note__iregex=radius) | Q(short_note__iregex=radius)
                 )
         elif shirina and visota and diametr and saler:
             a = Shine.objects.filter(shirina__contains=shirina).filter(visota__contains=visota)\
                 .filter(diametr__contains=diametr).filter(
                 Q(company__iregex=saler) | Q(company__iregex=saler)
                 )
         elif shirina and visota and diametr:
             a = Shine.objects.filter(shirina__contains=shirina).filter(visota__contains=visota) \
                 .filter(diametr__contains=diametr)
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

        def search(search_res):
            list_saler = []
            for el in search_res["ads"]:
                shir, vis, dia, dia_d = '', '', '', ''
                for elem in el["ad_parameters"]:
                    if elem["pl"] == "Ширина":
                        shir = elem["vl"]
                    if elem["pl"] == "Высота":
                        vis = elem["vl"]
                    if elem["pl"] == "Диаметр":
                        dia = str(elem["vl"])
                    if elem["pl"] == "Диаметр диска":
                        dia_d = str(elem["vl"])

                list_saler.append(
                    [el["ad_link"], el["subject"], el["price_byn"][:-2], shir, vis, dia[1:], dia_d[1:], key])
            return list_saler

        salers = {"Максим": "3186887", "Никита": "3558328", "Антон": "5409979", "Сергей": "887851"}
        list_salers = []

        for key, value in salers.items():
            search_res = requests.get(
                f'https://api.kufar.by/search-api/v1/search/rendered-paginated?size=200&atid={value}&cat=2075&cmp=1&sort=lst.d').json()
            list_saler = search(search_res)
            con = search_res["total"]
            print("Всего обьяв: ", con)

            if con > 200:
                search_res = requests.get(
                    f'https://api.kufar.by/search-api/v1/search/rendered-paginated?size=200&atid={value}&cat=2075&cmp=1&sort=lst.d&cursor=eyJ0IjoicmVsIiwiYyI6W3sibiI6Imxpc3RfdGltZSIsInYiOjE2OTUyOTUzMjkwMDB9LHsibiI6ImFkX2lkIiwidiI6MjA4NDM5MzA3fV0sImYiOnRydWV9').json()
                list_saler1 = search(search_res)
                for i in list_saler1:
                    if i not in list_saler:
                        list_saler.append(i)
            if con > 360:
                search_res = requests.get(
                    f'https://api.kufar.by/search-api/v1/search/rendered-paginated?size=32&atid={value}&cat=2075&cmp=1&sort=lst.d&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MTIsInBpdCI6IjI4Mjg1MDUyIn0=').json()
                list_saler2 = search(search_res)
                for i in list_saler2:
                    if i not in list_saler:
                        list_saler.append(i)
            if con > 384:
                search_res = requests.get(
                    f'https://api.kufar.by/search-api/v1/search/rendered-paginated?size=32&atid={value}&cat=2075&cmp=1&sort=lst.d&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MTMsInBpdCI6IjI4Mjg1MDUyIn0=').json()
                list_saler2 = search(search_res)
                for i in list_saler2:
                    if i not in list_saler:
                        list_saler.append(i)
            if con > 416:
                search_res = requests.get(
                    f'https://api.kufar.by/search-api/v1/search/rendered-paginated?size=32&atid={value}&cat=2075&cmp=1&sort=lst.d&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MTQsInBpdCI6IjI4Mjg1MDYzIn0=').json()
                list_saler2 = search(search_res)
                for i in list_saler2:
                    if i not in list_saler:
                        list_saler.append(i)
            if con > 448:
                search_res = requests.get(
                    f'https://api.kufar.by/search-api/v1/search/rendered-paginated?size=32&atid={value}&cat=2075&cmp=1&sort=lst.d&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MTUsInBpdCI6IjI4Mjg1MDcyIn0=').json()
                list_saler2 = search(search_res)
                for i in list_saler2:
                    if i not in list_saler:
                        list_saler.append(i)
            s = 0
            for pos in list_saler:
                s += 1
                pos.insert(0, s)
            list_salers.append(list_saler)

        r_count = 0
        for yy in list_salers:
            for xx in yy:
                a_1 = Shine(number=xx[0], href=xx[1], company=xx[8], shirina=xx[4], visota=xx[5],
                            diametr=xx[6], diametr_d=xx[7], price=xx[3], short_note=xx[2])
                a_1.save()
                r_count += 1
        b_1 = 'Получны новые данные! '
        time = datetime.now().strftime('%d-%m-%Y %H:%M')
        a_2 = Times.objects.all()
        a_2.delete()
        a_2 = Times(time1=time)
        a_2.save()

        return render(request, 'cards/search.html',
                      {"b_1": b_1, "r_count": r_count, "time": time})
    if request.method == "POST":
        return redirect('search')


