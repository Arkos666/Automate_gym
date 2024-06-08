import datetime
import os
import re
import time
from datetime import timedelta, date
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sys import platform


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    if platform == "linux" or platform == "linux2":
        path = "/usr/bin/chromedriver/"
        os.chmod(path, 0o0777)
        os.environ["PATH"] += os.pathsep + path
        print("PATH Chromedriver added")
    elif platform == "darwin":
        # OS X
        print("MAC")
    elif platform == "win32":
        # Windows...
        print("Windows")
    else:
        print("Other")

    substring = ""
    txt_hora = ""
    usr = ""
    pwd = ""

    print(date.today().strftime("%A"))
    if date.today().strftime("%A") == "Tuesday":
        hora = int(datetime.datetime.now().hour)

        if hora < 15:
            substring = "ESQUENA SANA"
            txt_hora = '09:30'
            usr = "53032274R"
            pwd = "11061982"
        else:
            substring = "SALSA CARDIO \\\\&quot;AL L.MIT\\\\&quot;"
            txt_hora = '18:15'
            usr = "38859752X"
            pwd = "A1982fcfi"

    elif date.today().strftime("%A") == "Sunday":
        hora = int(datetime.datetime.now().hour)

        if hora < 15:
            substring = "ESQUENA SANA"
            txt_hora = '10:30'
            usr = "53032274R"
            pwd = "11061982"
        else:
            substring = "SH\*BAM \\\\&quot;AL L.MIT\\\\&quot;"
            txt_hora = '19:15'
            usr = "38859752X"
            pwd = "A1982fcfi"

    print(substring)

    driver = webdriver.Chrome()
    vars = {}

    driver.get("https://gimnasiomataro.provis.es/Login")
    driver.set_window_size(1366, 741)
    driver.maximize_window()
    driver.find_element(By.ID, "Username").click()
    driver.find_element(By.ID, "Username").send_keys(usr)
    driver.find_element(By.ID, "Password").send_keys(pwd)
    driver.find_element(By.ID, "Password").send_keys(Keys.ENTER)
    print("Password and ENTER")

    EndDate = date.today() + timedelta(days=1)

    link = 'https://gimnasiomataro.provis.es/ActividadesColectivas/' \
           'ClasesColectivasTimeLine?modelo=&' \
           'fecha={}-{:02d}-{:02d}T00:00:00'.format(EndDate.year, EndDate.month, EndDate.day)

    time.sleep(3)
    print (link)
    driver.get(link)

    time.sleep(3)
    txt_html = driver.page_source

    text_file = open("sample.html", "w")
    n = text_file.write(txt_html)
    text_file.close()

    time.sleep(3)
    print("get html code for regex")

    txt_button = "button"
    txt_data_hora = '{}-{:02d}-{:02d}T' + txt_hora + ':00'.format(EndDate.year, EndDate.month, EndDate.day)

    txt_start = 'data-json="{&quot;Id&quot;:[0-9]{5},&quot;Nombre&quot;:&quot;'
    txt_end = '&quot;,&quot;HoraInicio&quot;:&quot;' \
              '[0-9]{4}-[0-9]{2}-[0-9]{2}T' + txt_hora + ':00'

    print ("SEARCH " + txt_start + substring + txt_end)

    txt = re.search(txt_start + substring + txt_end, txt_html)

    print(txt.group())

    btn_id = re.search('[0-9]{5}', txt.group()).group()
    print ("Button ID: " + btn_id)
    txt_time = txt.group()[-5:]

    print(btn_id + " - FOUND")
    btn = driver.find_element(By.ID, btn_id)

    print("BUTTON - FOUND")

    btn.click()

    time.sleep(3)
    print("button click => MODAL appears")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Scroll to end")

    btn_reserva_modal = driver.find_element(By.ID, "btnReserva")
    print("btnReserva Found?")
    time.sleep(3)

    btn_reserva_modal.click()
    print("btnReserva clicked")

    time.sleep(10)

    exit()
