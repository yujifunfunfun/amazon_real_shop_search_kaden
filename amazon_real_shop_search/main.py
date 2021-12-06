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
from engine.rakuten import *
from engine.yahoo import *
from engine.kakaku import *
from common.operation_csv import *
from common.chromedriver import *
import multiprocessing
from multiprocessing import freeze_support



def fetch_biccamera_edion_data(model_number_list,amazon_price_url_name_list):
    user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69"
]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    option0 = Options()                         
    # option.add_argument('--headless') 
    option0.add_argument('--user-data-dir=' + os.path.join(os.getcwd(),"profile0")) 
    option0.add_argument('--lang=ja-JP')
    option0.add_argument('--user-agent=' + UA)
    option0.add_argument('--ignore-certificate-errors')
    option0.add_argument('--ignore-ssl-errors')
    option0.add_argument("window-size=900,800")
    #ここで、バージョンなどのチェックをする
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option0) 
    
    biccamera_item_data = fetch_biccamera_data(driver,model_number_list)
    driver.quit()
    edion_item_data = fetch_edion_data(model_number_list)
    
    biccamera_edion_cal_profit(biccamera_item_data,edion_item_data,amazon_price_url_name_list)



def fetch_ks_laox_matsuya_data(model_number_list,amazon_price_url_name_list):
    user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69"
]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    option0 = Options()                         
    # option.add_argument('--headless') 
    option0.add_argument('--user-data-dir=' + os.path.join(os.getcwd(),"profile1")) 
    option0.add_argument('--lang=ja-JP')
    option0.add_argument('--user-agent=' + UA)
    option0.add_argument('--ignore-certificate-errors')
    option0.add_argument('--ignore-ssl-errors')
    option0.add_argument("window-size=900,800")
    #ここで、バージョンなどのチェックをする
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option0) 
    
    ks_item_data = fetch_ks_data(driver,model_number_list)
    laox_item_data = fetch_laox_data(driver,model_number_list)
    matsuya_item_data = fetch_matsuya_data(driver,model_number_list)
    driver.quit()
    
    ks_laox_matsuya_cal_profit(ks_item_data,laox_item_data,matsuya_item_data,amazon_price_url_name_list)
    
    
    
def fetch_nojima_yodobashi_data(model_number_list,amazon_price_url_name_list):
    user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69"
]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    option0 = Options()                         
    # option.add_argument('--headless') 
    option0.add_argument('--user-data-dir=' + os.path.join(os.getcwd(),"profile2")) 
    option0.add_argument('--lang=ja-JP')
    option0.add_argument('--user-agent=' + UA)
    option0.add_argument('--ignore-certificate-errors')
    option0.add_argument('--ignore-ssl-errors')
    option0.add_argument("window-size=900,800")
    #ここで、バージョンなどのチェックをする
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option0) 
    nojima_item_data = fetch_nojima_data(driver,model_number_list)
    yodobashi_item_data = fetch_yodobashi_data(driver,model_number_list)
    driver.quit()
    
    nojima_yodobashi_cal_profit(nojima_item_data,yodobashi_item_data,amazon_price_url_name_list)

def fetch_rakuten_yahoo_kakaku_kojima_data(jan_list,model_number_list,amazon_price_url_name_list):
    rakuten_item_data = fetch_rakuten_data(jan_list)
    yahoo_item_data = fetch_yahoo_data(jan_list)
    kakaku_item_data = fetch_kakaku_data(model_number_list)
    kojima_item_data = fetch_kojima_data(model_number_list)
    
    rakuten_yahoo_kakaku_kojima_cal_profit(rakuten_item_data,yahoo_item_data,kakaku_item_data,kojima_item_data,amazon_price_url_name_list)



def fetch_yamada_item_data(model_number_list,amazon_price_url_name_list):
    yamada_item_data = fetch_yamada_data(model_number_list)    
    yamada_cal_profit(yamada_item_data,amazon_price_url_name_list)

    

def main():
    model_number_list = load_model_number()
    jan_list = load_jan()
    logger.info('amazonデータ取得中...')
    amazon_price_url_name_list = fetch_amazon_price_url()

    p0 = multiprocessing.Process(target=fetch_biccamera_edion_data,args=(model_number_list,amazon_price_url_name_list))
    p1 = multiprocessing.Process(target=fetch_ks_laox_matsuya_data,args=(model_number_list,amazon_price_url_name_list))
    p2 = multiprocessing.Process(target=fetch_nojima_yodobashi_data,args=(model_number_list,amazon_price_url_name_list))
    p3 = multiprocessing.Process(target=fetch_rakuten_yahoo_kakaku_kojima_data,args=(jan_list,model_number_list,amazon_price_url_name_list))
    p4 = multiprocessing.Process(target=fetch_yamada_item_data,args=(model_number_list,amazon_price_url_name_list))
    
    

    # プロセス開始
    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    
        
    # プロセス終了待ち合わせ
    p0.join()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
    
    join_csv()
    
    
    
    
    
    
    
if __name__ == "__main__":
    freeze_support()
    main()

