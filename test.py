# import functools

# #*args pozwala przekazywac dowolna liczbe argumentow pozycyjnych (np. liczby) do funkcji - argumenty w funkcji sa dostepne jako tuple
# def dekorator(func):
#     @functools.wraps(func)
#     def funkcja_z_args(*args, **kwargs): 
#         print("Argumenty nazwane")
#         for arg in args:
#             print(arg)
#         wynik = func(**kwargs)
#         return wynik
#     return funkcja_z_args

# # funkcja_z_args(1, 2, 3,4,5)

# #**kwargs pozwala przekazywac zmienna liczbe argumentow nazwanych (wlasne nazwy) do funkcji - argumenty sa dostepne wewnatrz funkcji jako slownik
# def funkcja_z_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# # funkcja_z_kwargs(imie="Jan", nazwisko = "Kowalski", wiek = 30, miasto = "Warszawa")        

# #Mozna laczyc obie te rzeczy
# @dekorator
# def funkcja_udekorowana(**kwargs):
#     print("Argumenty nazwane")
#     for klucz, wartosc in kwargs.items():
#         print(f"{klucz} = {wartosc}")

# print(funkcja_udekorowana(1,2,3, imie = "Jan"))

input_number = int(input())
input_power = int(input())
for i in range(0,input_power+1):
    power_number = input_number**i
    print(f"{power_number}")
    