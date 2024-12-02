from library import *
from utils import Webscrape

######### PARAMETERS #########
url = "https://www.emag.hu/gyerekhazak-es-satrak/c?ref=subcat_1_fashion-grid_1"

######## MAIN FUNC ##########

def main():
    wc = Webscrape()    
    driver = wc.initialize_webdriver(url)
    big = wc.get_data(driver=driver)
    df, aggr_df = wc.create_df(big)
    df
    aggr_df
    
######## RUN ################
main()





