""" Runs the script for webscraping """

from library import *
from utils import Webscrape

######### PARAMETERS #########
url = "https://www.emag.hu/gyerekhazak-es-satrak/c?ref=subcat_1_fashion-grid_1"
buffer = 50
######## MAIN FUNC ##########

def main():
    wc = Webscrape()    
    driver = wc.initialize_webdriver(url)
    big = wc.get_data(driver=driver,buffer=buffer)
    df, aggr_df = wc.create_df(big)
    print(df)
    print(aggr_df)
    
######## RUN ################
main()





