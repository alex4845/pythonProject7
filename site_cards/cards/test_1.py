from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.kufar.by")
time.sleep(2)
click_1 = driver.find_element(By.XPATH, """//*[@id="__next"]/div[4]/div/div[2]/button""")
click_1.click()#куки
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
    print(name, "Количество страниц____________", n_p)
    n = 0
    for i in range(0, n_p):
        wills = driver.find_elements(By.CLASS_NAME, "styles_wrapper__pb4qU")
        for will in wills:
            ss = will.get_attribute("href")
            short_note = will.find_element(By.CLASS_NAME, "styles_title__wj__Y")
            price = will.find_element(By.CLASS_NAME, "styles_price__x_wGw")
            #print(ss)
            n += 1
            list.append(will.text)
            print(n, short_note.text, price.text, name)
        if i == n_p - 1: break
        elif i == 0:
            number = pag + """1]"""
        elif i >= 4:
            number = pag + """4]"""
        else:
            number = pag + str(i + 2) + """]"""
        driver.find_element(By.XPATH, number).click()
        time.sleep(2)
print(len(list), "всего")







