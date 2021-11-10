from engine.biccamera import *
from engine.edion import *
from engine.kojima import *
from engine.ks import *
from engine.laox import *
from engine.matsuya import *
from engine.nojima import *
from engine.yamada import *
from engine.yodobashi import *
from engine.amazon import *
from engine.cal_profit import *
from common.csv import *
from common.chromedriver import *



def main():
    driver = start_chrome()
    model_number_list = load_model_number()
    biccamera_item_data = fetch_biccamera_data(driver,model_number_list)
    edion_item_data = fetch_edion_data(driver,model_number_list)
    kojima_item_data = fetch_kojima_data(driver,model_number_list)
    ks_item_data = fetch_ks_data(driver,model_number_list)
    laox_item_data = fetch_laox_data(driver,model_number_list)
    matsuya_item_data = fetch_matsuya_data(driver,model_number_list)
    nojima_item_data = fetch_nojima_data(driver,model_number_list)
    yamada_item_data = fetch_yamada_data(driver,model_number_list)
    yodobashi_item_data = fetch_yodobashi_data(driver,model_number_list)
    driver.quit()
    
    amazon_price_url_list = fetch_amaozn_price_url()
    
    cal_profit(biccamera_item_data,edion_item_data,kojima_item_data,ks_item_data,laox_item_data,matsuya_item_data,nojima_item_data,yamada_item_data,yodobashi_item_data,amazon_price_url_list)
    
    
    
    
if __name__ == "__main__":
    main()