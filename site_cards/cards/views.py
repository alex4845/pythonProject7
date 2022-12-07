import os

from PIL import Image
from django.db.models import Max
from django.shortcuts import render, redirect
from datetime import datetime, date, timedelta

from cards.forms import ShineForm
from cards.models import Shine
import requests
from bs4 import BeautifulSoup as BS


def main_page(request):

    return render(request, 'cards/index.html')


def add_card(request):
    if request.method == "GET":
        form = ShineForm()
        return render(request, 'cards/add_card.html', {"form": form})

    if request.method == "POST":
        form = ShineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            a = form
            img_obj = form.instance
        return render(request, 'cards/add_card.html', {"a": a, "img_obj": img_obj})


def search(request):
     if request.method == "GET":
         return render(request, 'cards/search.html')

     if request.method == "POST":
         radius = request.POST["radius"]
         shirina = request.POST["shirina"]
         visota = request.POST["visota"]
         date = request.POST["date"]

         if radius and shirina and visota:
             a = Shine.objects.filter(radius=radius, shirina=shirina, visota=visota)
         elif radius and shirina:
             a = Shine.objects.filter(radius=radius, shirina=shirina)
         elif radius:
             a = Shine.objects.filter(radius=radius)
         elif shirina:
             a = Shine.objects.filter(shirina=shirina)
         elif visota:
             a = Shine.objects.filter(visota=visota)
         elif date:
             a = Shine.objects.filter(enter_date=date)

         else:
             a = Shine.objects.all()
         b = "Шины с такими параметрами не обнаружены"
         return render(request, 'cards/search.html', {"a": a, "b": b})


def del_card(request, pk):
    a = Shine.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'cards/action.html', {"a": a})
    if request.method == "POST":
        if request.POST["delete"] == "Удалить запись":
            a.image.delete(save=True)
            a.delete()
            b = "Запись удалена"
            return render(request, 'cards/action.html', {"b": b})

        if request.POST["delete"] == "Внести исправления":
            c, b = "", ""
            if request.POST["note_1"]:
                a.note = request.POST["note_1"]
                b = "Примечание исправлено"
            if request.POST["cost"]:
                a.cost = request.POST["cost"]
                c = "Цена исправлена"
            a.save()
            return render(request, 'cards/action.html', {"a": a, "b": b, "c": c})

def ubdate(request):
    if request.method == "GET":
        r = requests.get("https://www.kufar.by/user/3186887")
        html = BS(r.content, 'html.parser')
        c = html.select('.styles_wrapper__pb4qU')

        for i in c:
            p = i.get("href")
            par = requests.get(p)
            html_1 = BS(par.content, 'html.parser')
            note = html_1.select('.styles_description_content__Lj7Ik')
            parameters = []
            a = Shine()
            for i in note:
                parameters.append(i.text)
            sp = Shine.objects.filter(note=parameters[0])
            if sp: continue
            a.note = parameters[0]

            imgs = html_1.select('.styles_slide__image__lc2v_')
            s = 0
            for i in imgs:
                res = i.get("src")
                im = requests.get(res, stream=True).content
                if not os.path.exists('media/media/site_cards'):
                    os.makedirs('media/media/site_cards')
                with open('media/media/site_cards/' + res[49:59] + '.jpg', "wb") as handler:
                    handler.write(im)
                if s == 0:
                    a.image = 'media/site_cards/' + res[49:59] + '.jpg'
                # elif s == 1:
                #     a.image_1 = 'media/site_cards/' + res[49:59] + '.jpg'
                # elif s == 2:
                #     a.image_2 = 'media/site_cards/' + res[49:59] + '.jpg'
                s += 1
                a.save()


    return redirect('search')




