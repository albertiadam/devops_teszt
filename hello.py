from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

page_url = "https://www.emag.hu/televiziok/filter/kijelzo-technologia-f8914,led-v-4670591/c?ref=hp_menu_quick-nav_43_1&type=link"
driver = webdriver.Chrome()
driver.get(page_url)
big = []
for x in range(100):
    try:
        fasz = driver.find_elements(By.XPATH, f'//*[@id="card_grid"]/div[{x}]/div/div/div[3]/div/h2/a')
        asd = driver.find_elements(By.XPATH, f'//*[@id="card_grid"]/div[{x}]/div/div/div[4]/div[1]/p[2]')
        zsar = driver.find_elements(By.XPATH, f'//*[@id="card_grid"]/div[{x}]/div/div/div[3]/div/div[1]/a/div[2]/span[1]')
        print(fasz[0].text, asd[0].text, zsar[0].text)
        lista = [fasz[0].text,asd[0].text,zsar[0].text]
        big.append(lista)
    except:
        print("")
        

tvk = pd.DataFrame(big)
tvk = tvk.rename(columns={0:'Név',1:'Ár',2:'Értékelés'})
tvk['Ár'] = tvk['Ár'].apply(lambda x: int(x[:-3].replace(".","")))
tvk = tvk.sort_values(by=['Ár','Értékelés'])

asd = tvk['Ár'].aggregate({
    'Átlag' : 'mean',
    'Maximum' : 'max',
    'Minimum' : 'min'
})
