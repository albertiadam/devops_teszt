from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def initialize_webdriver(url:str) -> webdriver:
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def get_data(driver:webdriver,buffer:int) -> list:
    """Summary
        Gathers the data from the given url, by predefined xpath
    Args:
        driver (webdriver): Driver used for the browser with the opened site
        buffer (int): The number of elements to iterate through
    Returns:
        list: Returns the gathered data by xpath from the site
    """
    data = []
    for x in range(buffer):
        try:
            name = driver.find_elements(By.XPATH, f'//*[@id="card_grid"]/div[{x}]/div/div/div[3]/div/h2/a')
            price = driver.find_elements(By.XPATH, f'//*[@id="card_grid"]/div[{x}]/div/div/div[4]/div[1]/p[2]')
            rating = driver.find_elements(By.XPATH, f'//*[@id="card_grid"]/div[{x}]/div/div/div[3]/div/div[1]/a/div[2]/span[1]')
            picture = driver.find_elements(By.XPATH, f'//*[@id="card_grid"]/div[{x}]/div/div/div[3]/a/div[1]/img')[0].get_attribute("src")
            print(name[0].text, price[0].text, rating[0].text)
            sub_list = [name[0].text,price[0].text,rating[0].text,picture]
            data.append(sub_list)
        except Exception:
            print("")
    driver.quit()
    return data

url = "https://www.emag.hu/mobiltelefonok/c?ref=hp_menu_quick-nav_1_1&type=category"
buffer = 60
driver = initialize_webdriver(url)
big = get_data(driver=driver,buffer=buffer)

df = pd.DataFrame(big)
df.columns = ['Név','Ár','Értékelés','Kép link']
df.to_excel("telok.xlsx")

asd = driver.find_elements(By.XPATH,'//*[@id="card_grid"]/div[1]/div/div/div[3]/a/div[1]/img')[0].get_attribute("src")

print(df)


