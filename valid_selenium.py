from selenium import webdriver
from selenium.webdriver.common.by import By

def validalas():
    # Hozz létre egy Firefox driver példányt!
    driver = webdriver.Firefox()

    # Töltse be az oldaladat
    driver.get("http://localhost/nincs/valid_selenium/")

    # A nevek alapján kerestessük meg az űrlap elemeit!
    f_nev = driver.find_element(By.NAME,"fNev")
    jelszo = driver.find_element(By.NAME,"jsz")


    
    # ... 
    # A következő elemet nem kell átírnod:
    submit_gomb = driver.find_element(By.XPATH,"//input[@type='submit']")

    # Add meg a működő - majd később a nem működő - teszt adatokat!
    k_nev.send_keys("Kornel")
    jelszo.send_keys("Alma123")

    # ...

    # Kattints a submit gombra!
    submit_gomb.click()

    # Várunk egy keveset, hogy lássunk is valamit...
    driver.implicitly_wait(10)

    # Megnézzük, megjelent-e a div elemünk
    success_message = driver.find_element(By.XPATH,"//div[@class='success-message']")
    if success_message.is_displayed():
        print("Sikerült az űrlap küldése!")
    else:
        print("Nem sikerült az űrlap küldése!")

    # Csukjuk be a böngésző ablakot!
    driver.quit()
