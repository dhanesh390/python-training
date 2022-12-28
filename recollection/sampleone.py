import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL = "https://realpython.github.io/fake-jobs/"
# URl = "https://https://realpython.com/beautiful-soup-web-scraper-python/"
# page = requests.get(URL)
# print(page.text)
# soup = BeautifulSoup(page.content, "html.parser")


baseurl = "https://www.flipkart.com/"
# page_two = requests.get(baseurl)
# print(page_two.text)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

product_one = requests.get(
    'https://www.flipkart.com/tyy/4io/~cs-e0objcvf4c/pr?sid=tyy,4io&collection-tab-name=Realme+10+pro+5g&param=49201&otracker=clp_banner_1_15.bannerX3.BANNER_mobile-phones-store_1MVT8BYQY739&fm=neo%2Fmerchandising&iid=M_22a8f7fc-4081-484d-89bb-ec7799e72943_15.1MVT8BYQY739&ppt=hp&ppn=homepage&ssid=mm54l4aggw0000001672050194976').text

soup = BeautifulSoup(product_one, 'html.parser')

product_list = soup.find_all("div", {"class": "_1D76KH"})  # _1AtVbE
print(product_list)

product_links = [] #
for product in product_list:
    link = product.find("a", {"class": "_1D76KH"}).get('href')
    product_links.append(baseurl + link)
print(product_links)
