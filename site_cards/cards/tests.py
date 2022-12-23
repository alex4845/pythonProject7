from selenium import webdriver
from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.kufar.by")
time.sleep(2)
click_1 = driver.find_element(By.XPATH, """//*[@id="__next"]/div[3]/div/div[2]/button""")
click_1.click()#куки
time.sleep(2)
category = driver.find_element(By.CLASS_NAME, "styles_chip__icon__fBw77")
category.click()
time.sleep(2)

list_com = ["https://www.kufar.by/user/3186887",
            "https://www.kufar.by/user/3558328",
            "https://www.kufar.by/user/2938958",
            "https://www.kufar.by/user/5409979"
            ]
s, m = [], 0
for el in list_com:
    driver.get(el)
    time.sleep(3)
    click_2 = driver.find_element(By.XPATH, """//*[@id="shop_filtres_wrapper"]/div[1]/button[2]/span""")
    click_2.click()#выбор шины-диски
    time.sleep(3)
    name_comp = driver.find_element(By.CLASS_NAME, "styles_pro-user-widget__info-title__7ejw5")
    name_c = name_comp.text
    count_pages = driver.find_element(By.CLASS_NAME, "styles_pagination__inner__Jd_T_")
    n_p = int(count_pages.text[-2] + count_pages.text[-1])
    print("Количество страниц", name_c, n_p, "-------------------------------")
    n, count = 0, 0
    next_p = ["""//*[@id="__next"]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/div/div/a[4]""",
              """/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/a[5]""",
              """//*[@id="__next"]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/a[4]""",
              """//*[@id="__next"]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/a[2]"""
              ]
    while n < n_p:
        will_element = driver.find_elements(By.CLASS_NAME, "styles_left___v6uP")
        for i in will_element:
            count += 1
            s.append(i.text)
            print(count, i.text, name_c)
        click_3 = driver.find_element(By.XPATH, next_p[m])
        click_3.click()
        n += 1
        time.sleep(10)

    m += 1




