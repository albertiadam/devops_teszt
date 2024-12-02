from library import *
class Webscrape:
    def __init__(self):
        """Init func"""
    def initialize_webdriver(self,url:str) -> webdriver:
        page_url = "https://www.emag.hu/gyerekhazak-es-satrak/c?ref=subcat_1_fashion-grid_1"
        driver = webdriver.Chrome()
        driver.get(page_url)
        return driver

    def get_data(self,driver) -> list:
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
        return big

    def create_df(self,data_list:list) -> tuple:
        tvk = pd.DataFrame(data_list)
        tvk = tvk.rename(columns={0:'Név',1:'Ár',2:'Értékelés'})
        tvk['Ár'] = tvk['Ár'].apply(lambda x: int(x[:-3].replace(".","")))
        tvk = tvk.sort_values(by=['Ár','Értékelés'])

        asd = tvk['Ár'].aggregate({
            'Átlag' : 'mean',
            'Maximum' : 'max',
            'Minimum' : 'min'
        })
    
        return tvk,asd   
