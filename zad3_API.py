"""
Za pomocą API zwracającego informacje dot. uniwersytetów w danym państwie:
http://universities.hipolabs.com/search?country=<nazwa_kraju_eng>
wyświetl nazwy uniwersytetów z 15 wybranych krajów w postaci:
{<nazwa_kraju>: [<nazwa_uniwersytet1>, <nazwa_uniwersytet2>,...], …}.
W celu przyspieszenia pobierania danych, wykorzystaj moduł threading do realizacji
wielowątkowego pobierania informacji.
"""

import requests
import threading
import concurrent.futures
import random
from bs4 import BeautifulSoup

COUNTRIES_NUMBER = 15

        
if __name__ == "__main__":

    url = "http://universities.hipolabs.com/search?country="    
    resp = requests.get(url)
    universities = resp.json()

    countries = set() #Zapobieganie powtorzeniom

    for university in universities:
        country = university['country'] # country to klucz slownika university
        if country:
            countries.add(country)
    
    all_country_list, random_countries = [], []
    for country in countries:
        all_country_list.append(country)
    
    random_countries = random.sample(all_country_list, COUNTRIES_NUMBER)
    # print(f"All random countries: \n{random_countries}\n First random country: {random_countries[0]} ")
    
    for i in range(COUNTRIES_NUMBER):
        print(random_countries[i]) 
    













# def thread_function(number):
#     logging.info(f"Watek %d: rozpoczal sie {number}")
#     time.sleep(2)
#     logging.info(f"Watek %d: zakonczyl sie {number}")    

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
    
#     with concurrent.futures.ThreadPoolExecutor(max_workers=24) as executor:
#         executor.map(thread_function, range(24))