# # import functools

# # #*args pozwala przekazywac dowolna liczbe argumentow pozycyjnych (np. liczby) do funkcji - argumenty w funkcji sa dostepne jako tuple
# # def dekorator(func):
# #     @functools.wraps(func)
# #     def funkcja_z_args(*args, **kwargs): 
# #         print("Argumenty nazwane")
# #         for arg in args:
# #             print(arg)
# #         wynik = func(**kwargs)
# #         return wynik
# #     return funkcja_z_args

# # # funkcja_z_args(1, 2, 3,4,5)

# # #**kwargs pozwala przekazywac zmienna liczbe argumentow nazwanych (wlasne nazwy) do funkcji - argumenty sa dostepne wewnatrz funkcji jako slownik
# # def funkcja_z_kwargs(**kwargs):
# #     for key, value in kwargs.items():
# #         print(f"{key} = {value}")

# # # funkcja_z_kwargs(imie="Jan", nazwisko = "Kowalski", wiek = 30, miasto = "Warszawa")        

# # #Mozna laczyc obie te rzeczy
# # @dekorator
# # def funkcja_udekorowana(**kwargs):
# #     print("Argumenty nazwane")
# #     for klucz, wartosc in kwargs.items():
# #         print(f"{klucz} = {wartosc}")

# # print(funkcja_udekorowana(1,2,3, imie = "Jan"))

# input_number = int(input())
# input_power = int(input())
# for i in range(0,input_power+1):
#     power_number = input_number**i
#     print(f"{power_number}")
    
import requests
from concurrent.futures import ThreadPoolExecutor
import random

COUNTRIES_NUMBER = 15
MAX_THREAD_NUMBER = 16

def fetch_universities_for_country(country):
    url = f"http://universities.hipolabs.com/search?country={country}"
    response = requests.get(url)
    return country, [uni['name'] for uni in response.json()]

if __name__ == "__main__":
    url = "http://universities.hipolabs.com/search"
    univer_resp = requests.get(url)
    universities = univer_resp.json()
    countries = set()  # Zapobieganie powtórzeniom
    
    for university in universities:
        country = university['country']  # country to klucz słownika university
        if country:
            countries.add(country)
        
    all_country_list = list(countries)
    random_countries = random.sample(all_country_list, COUNTRIES_NUMBER)
         
    country_universities = {}

    # Używanie ThreadPoolExecutor do równoległego pobierania informacji
    with ThreadPoolExecutor(max_workers=MAX_THREAD_NUMBER) as executor:
        future_to_country = {executor.submit(fetch_universities_for_country, country): country for country in random_countries}

        for future in future_to_country:
            country, universities = future.result()
            country_universities[country] = universities

    for country, universities in country_universities.items():
        print(f"\nCountry: {country}")
        for university in universities:
            print(f"- {university}")
