""" Purpose of this file is to gather name, price and rating for different products from emag, then put them into a df and aggregate them """

from library import *
class Webscrape:
    def __init__(self):
        """Init func"""
    def initialize_webdriver(self,url:str) -> webdriver:
        page_url = "https://www.emag.hu/gyerekhazak-es-satrak/c?ref=subcat_1_fashion-grid_1"
        driver = webdriver.Chrome()
        driver.get(page_url)
        return driver

    def get_data(self,driver:webdriver,buffer:int) -> list:
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
                print(name[0].text, price[0].text, rating[0].text)
                sub_list = [name[0].text,price[0].text,rating[0].text]
                data = []
            except:
                print("")
        driver.quit()
        return data

    def create_df(self,data_list:list) -> tuple:
        """Summary

        Args:
            data_list (list): Gathered data, output of get_data()

        Returns:
            tuple: 2 df, one with all data, one which is aggregated by mean,min,max
        """
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
