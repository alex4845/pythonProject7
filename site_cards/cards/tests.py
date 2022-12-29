
#Парсинг фото и сохранение их в бд

from django.contrib.sites import requests

imgs = html_1.select('.styles_slide__image__lc2v_')
s = 0
for i in imgs:
    if s > 3: break
    res = i.get("src")
    im = requests.get(res, stream=True).content
    if not os.path.exists('media/media/site_cards'):
        os.makedirs('media/media/site_cards')
    with open('media/media/site_cards/' + res[49:59] + '.jpg', "wb") as handler:
        handler.write(im)
    if s == 0:
        a_1.image = 'media/site_cards/' + res[49:59] + '.jpg'
    elif s == 1:
        a_1.image_1 = 'media/site_cards/' + res[49:59] + '.jpg'
    elif s == 2:
        a_1.image_2 = 'media/site_cards/' + res[49:59] + '.jpg'
    elif s == 3:
        a_1.image_3 = 'media/site_cards/' + res[49:59] + '.jpg'
    s += 1
    a_1.save()