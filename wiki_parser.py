from bs4 import BeautifulSoup
import requests
import json
from fake_useragent import UserAgent

input_url = input('Enter Wiki page:')

ua = UserAgent()

def get_data(url):
    headers = {
        "User-Agent": ua.random
    }

    url = input_url
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'lxml')
    data = soup.find_all('table', class_='infobox hproduct')
    cars = []
    
    def car_info(data):
        for i in data:
            manufacturer_find = i.find('th', string='Manufacturer').next_sibling
            manufacter=(f'Manufacturer: {manufacturer_find.text}')

            production_find = i.find('th', string='Production').next_sibling
            production=(f'Production: {production_find.text}')

            car_class_find = i.find('th', string='Class').next_sibling
            car_class=(f'Class: {car_class_find.text}')

            cars.append(
                {
                    'manufacter': manufacter,
                    'production': production,
                    'class': car_class
                }
            )
            break
    
    car_info(data)

    def save_data(cars):
        with open(f'data.json', 'w', encoding='utf=8') as jfile:
            json.dump(cars, jfile, indent=4, ensure_ascii=False)

    save_data(cars)

get_data(f"{input_url}")