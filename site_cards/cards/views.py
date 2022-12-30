
import shutil

from django.db.models import Q
from django.shortcuts import render, redirect
from datetime import datetime, date, timedelta

from cards.forms import ShineForm
from cards.models import Shine
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def main_page(request):

    return render(request, 'cards/index.html')

def report(request):
    if request.method == "GET":
        return render(request, 'cards/report.html')

    if request.method == "POST":
        saler = request.POST["saler"]
        if saler:
            if saler == "все":
                a = Shine.objects.all()
            else:
                a = Shine.objects.filter(company__icontains=saler)
            byn_2 = 0
            repid = []
            for i in a:
                pp = Shine.objects.filter(price=i.price, short_note=i.short_note, index=i.index)
                if len(pp) >= 2:
                    for e in pp:
                        repid.append(e.number)
                    repid.append(i.short_note)
                byn = i.price
                byn_1 = ""
                b = str(i.company)
                for el in str(byn):
                    if el.isdigit():
                        byn_1 = byn_1 + el
                    elif el == "р": break
                if byn_1 == "": by = 0
                else: by = int(byn_1)
                byn_2 = byn_2 + by
            if saler == "все": b = "всех продавцов"

            return render(request, 'cards/report.html',
                          {"b": b, "byn_2": byn_2, "repid": repid})

def search(request):
     if request.method == "GET":
         return render(request, 'cards/search.html')

     if request.method == "POST":
         radius = request.POST["radius"]
         shirina = request.POST["shirina"]
         saler = request.POST["saler"]
         if radius:
             a = Shine.objects.filter(
                 Q(short_note__iregex=radius) | Q(short_note__iregex=radius)
                 )
         elif shirina:
             a = Shine.objects.filter(index__contains=shirina)
         elif saler:
             a = Shine.objects.filter(
                 Q(company__iregex=saler) | Q(company__iregex=saler)
                 )
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
            a.image_1.delete(save=True)
            a.image_2.delete(save=True)
            a.image_3.delete(save=True)
            a.delete()
            b = "Запись удалена!"
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
        a = Shine.objects.all()
        a.delete()#очистка бд
        #shutil.rmtree('media/media/site_cards')#удаление фоток

        driver = webdriver.Chrome()
        driver.get("https://www.kufar.by")
        time.sleep(2)
        click_1 = driver.find_element(By.XPATH, """//*[@id="__next"]/div[4]/div/div[2]/button""")
        click_1.click()  # куки
        time.sleep(2)

        company = ["3186887", "3558328", "5409979", "2938958"]
        pag = """//*[@id="__next"]/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div/a["""
        list = []

        for el in range(0, len(company)):
            driver.get("https://www.kufar.by/user/" + company[el])
            time.sleep(2)
            category = driver.find_element(By.CLASS_NAME, "styles_chip__icon__fBw77")
            category.click()
            time.sleep(2)
            choise = driver.find_element(By.XPATH, """//*[@id="mobile-categories"]/div/div/div[2]/button[2]""")
            choise.click()
            time.sleep(2)  # диски-шины
            name_company = driver.find_element(By.CLASS_NAME, "styles_pro-user-widget__info-title__7ejw5")
            name = str(name_company.text)
            count_pages = driver.find_element(By.CLASS_NAME, "styles_pagination__inner__Jd_T_")
            n_p = int(count_pages.text[-2] + count_pages.text[-1])
            n = 0
            for i in range(0, n_p):
                wills = driver.find_elements(By.CLASS_NAME, "styles_wrapper__pb4qU")
                for will in wills:
                    ss = will.get_attribute("href")
                    short_note = will.find_element(By.CLASS_NAME, "styles_title__wj__Y")
                    price = will.find_element(By.CLASS_NAME, "styles_price__x_wGw")
                    index = will.find_element(By.CLASS_NAME, "styles_parameters__baZ7_.styles_ellipsis__3MoMa")
                    n += 1
                    a_1 = Shine(href=ss, short_note=short_note.text, price=price.text,
                                company=name, number=n, index=index.text)
                    a_1.save()
                    list.append(will.text)
                if i == n_p - 1:
                    break
                elif i == 0:
                    number = pag + """1]"""
                elif i >= 4:
                    number = pag + """4]"""
                else:
                    number = pag + str(i + 2) + """]"""
                driver.find_element(By.XPATH, number).click()
                time.sleep(2)

        r_count = len(list)
        b_1 = 'Получны новые данные! '
        return render(request, 'cards/search.html',
                      {"b_1": b_1, "r_count": r_count})
    if request.method == "POST":
        return redirect('search')


