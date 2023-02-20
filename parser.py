from bs4 import BeautifulSoup
import requests
import json
import time
import random
from fake_useragent import UserAgent
ua = UserAgent()

def get_data(url):
    headers = {
        "User-Agent": ua.random
    }

    links_count = 5
    print(f'Всего страниц {links_count}')

    for links in range(0, 6):
        req = requests.get(url + f'?page={links}', headers=headers)

        with open(f'cloth_{links}.html', 'w') as file:
            file.write(req.text)

        with open(f'cloth_{links}.html') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        block = soup.find_all('li', class_='producto col-md-3 col-lg-3 col-sm-4 col-xs-6')

        products = []

        for i in block:
            title_find = i.find('div', class_='name noOpt')
            title=(title_find.text.replace('\n', '')) # название продукта

            price_find = i.find('div', class_='price row').find('span', class_='curent noOpt')
            price=(price_find.text.replace('\n','')) # цена продукта

            link_find = i.find('div', class_='name noOpt').find('a').get('href')
            link=('https://issaplus.com'+link_find) # ссылка продукта

            products.append(
                {
                    'Title': title,
                    'Price': price,
                    'Link': link,
                    # 'Discount': discount or nodiscount
                }
            )

            # time.sleep(random.randrange(2, 4))

        # print(title+'\n'+price+'\n'+link+'\n') # вывод данных

    with open(f'data_{links}.json', 'w', encoding='utf=8') as jfile:
        json.dump(products, jfile, indent=4, ensure_ascii=False)
print('done')
get_data("https://issaplus.com/odezhda/")



        # picture_find = i.find('div', class_='images').find('img', itemprop="image").get('src')
        # print(picture_find)

        # try:
        #     discount_find = i.find('div', class_='badge low-price')
        #     discount = discount_find.text
        # except:
        #     nodiscount=('No discount')