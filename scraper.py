import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.ca/Yes4All-Solid-Competition-Kettlebell-Weight/dp/B06XRBBB5V/?_encoding=UTF8&pd_rd_w=C85bi&content-id=amzn1.sym.45d682ac-22ed-4836-a2a3-54cdaf4102de%3Aamzn1.symc.43e4e477-9c69-4a02-84f5-6da0b435879b&pf_rd_p=45d682ac-22ed-4836-a2a3-54cdaf4102de&pf_rd_r=J098150VFJMZ1HFEDY14&pd_rd_wg=g3w1K&pd_rd_r=7258ba7c-da91-4955-805f-aabae4d7a96b&ref_=pd_hp_d_atf_ci_mcx_mr_hp_atf_m&th=1'

headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'accept-language': 'en-GB,en;q=0.9', # need to use accept-language to scrape!
    }

page = requests.get(URL, headers=headers)

# print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

title = soup.find(id="productTitle").get_text()

print(title.strip())