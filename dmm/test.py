import requests
from bs4 import BeautifulSoup
import re



ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)" \
        "AppleWebKit/537.36 (KHTML, like Gecko)" \
        "Chrome/95.0.4638.69"

url = 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021092583292/?dmmref=gMonoHobby_Ranking_Figure_Week'
res = requests.get(url,headers={"User-Agent": ua})
soup = BeautifulSoup(res.text, "html.parser")


jan = soup.select("table.mg-b20")


jan = jan[0].text

p = r'JAN:\s(.*)'  
jan = re.search(p, jan).group(1)      
jan = re.sub(r'\D', '', jan) 

print(jan)


# for price in prices:
#         price = price.text
#         p = r'(.*)円'  
#         keyword = re.search(p, price).group(1)      
#         price = re.sub(r'\D', '', keyword) 
          
#         print(price)
        

# for url in urls:
#         url = url.get('href')
#         url = 'https://www.dmm.com' + url
#         print(url)
        
