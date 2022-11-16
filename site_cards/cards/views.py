from django.db.models import Max
from django.shortcuts import render, redirect
from datetime import datetime, date, timedelta

from cards.forms import CardForm
from cards.models import Cards


def main_page(request):
    date_now = datetime.now()
    a = Cards.objects.all()
    for i in a:
        if i.end_date <= date_now:
            i.status = "deactiv"
            i.save()

    return render(request, 'cards/index.html')


def add_card(request):
    if request.method == "GET":
        form = CardForm()
        return render(request, 'cards/add_card.html', {"form": form})

    if request.method == "POST":
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            a = form
        return render(request, 'cards/add_card.html', {"a": a})


def generator(request):
    if request.method == "GET":
        return render(request, 'cards/generator.html')
    if request.method == "POST":
        number = Cards.objects.all().aggregate(Max('number'))
        seria = request.POST["Серия"]
        term = request.POST["Срок"]
        if term == "r_1":
            end_date = datetime.now(tz=None) + timedelta(days=365)
        elif term == "r_2":
            end_date = datetime.now() + timedelta(days=183)
        elif term == "r_3":
            end_date = datetime.now() + timedelta(1)

        amount = request.POST["Количество"]
        s = number['number__max']
        k = 0
        while k < int(amount):
            k += 1
            s += 1
            a = Cards(serie=seria, number=s, status='activ', end_date=end_date)
            a.save()
        return render(request, 'cards/generator.html', {"a": a})


def search(request):
    if request.method == "GET":
        return render(request, 'cards/search.html')
    if request.method == "POST":
        status = request.POST["Статус"]
        seria = request.POST["Серия"]
        number = request.POST["Номер"]
        if status:
            a = Cards.objects.filter(status=status)
        if seria:
            a = Cards.objects.filter(serie=seria)
        if number:
            a = Cards.objects.filter(number=number)
        b = "Карты с такими параметрами не обнаружены"

        return render(request, 'cards/search.html', {"a": a, "b": b})

def del_card(request, pk):
    a = Cards.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'cards/action.html', {"a": a})

    if request.method == "POST":
        if request.POST["status"] == "Изменить статус карты":
            if a.status == "activ": a.status = "deactiv"
            elif a.status == "deactiv": a.status = "activ"
            a.save()
            s = "Статус изменен"
            return render(request, 'cards/action.html', {"a": a, "s": s})
        if request.POST["status"] == "Удалить карту":
            a.delete()
            b = "Карта удалена"
            return render(request, 'cards/action.html', {"b": b})
