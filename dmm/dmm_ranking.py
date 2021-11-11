import requests
from bs4 import BeautifulSoup
import re




def fetch_dmm_ranking_data():
    ranking_url = 'https://www.dmm.com/mono/hobby/-/ranking/=/mode=figure/term=week/rank=1_20/'
    res = requests.get(ranking_url)
    soup = BeautifulSoup(res.text, "html.parser")
    names = soup.select("div.data > p")
    prices = soup.select("div.data > div.red")
    urls = soup.select("td.bd-b > a")
    name_price_url_jan_list = []
    for name_elem,price_elem,url_elem in zip(names,prices,urls):
        name = name_elem.text
        
        price = price_elem.text
        p = r'(.*)円'  
        price = re.search(p, price).group(1)      
        price = re.sub(r'\D', '', price) 
        
        url = url_elem.get('href')
        url = 'https://www.dmm.com' + url
        
        res = requests.get(url)
        item_detail_soup = BeautifulSoup(res.text, "html.parser")
        