from audioop import reverse
from turtledemo.chaos import jumpto

# f(x, y) = x+y

# print(len(a),type(a))
# print(len(b),type(b))

# print(b.replace("anticipate","parlamentare"))
# a = "God is dead and we have killed Him"
# print(a.upper())
# print(a.lower())
# hero = "odiseu"
# hero2 = "ahile"
# print("ahile".islower().isupper())

# title = "Eu Robotul"
# random_title = "123"
# a = ["@", "!", " "]
# print(random_title.isdigit())

# print(title.isalpha())
#print(title)
# random_title2 = "test123"
# print(random_title2.isalnum())

# Colectii de date
# Liste

# Mutabile
# Indexabile
# Eterogene

# a = [1, 2, 3, 4, "caras"]
# print(a[::-1])

# b = "Pastrav"
# b[1] = "x"
# a[1] = 'x'
# print(a[4][2])

# school_of_fish = ["crap", "salau", "mreana","somn","somn","somn","salau"]

# school_of_fish.append("platica")
# school_of_fish.append(3)
# school_of_fish.append(["biban", "somn"])
# ['crap', 'salau', 'mreana', ['biban', 'somn']]
#school_of_fish.extend(["biban", "somn"])
# school_of_fish.extend("platica")
# print(school_of_fish)
#school_of_fish.clear()
#print(school_of_fish)
# print(school_of_fish.count("somon"))
# print(len(school_of_fish))
# school_of_fish = ["crap", "salau", "mreana","somn","somn","somn","salau"]
# fish = school_of_fish.copy()
#
# school_of_fish.append("pastrav")
# print("This is the school of fish list->", school_of_fish)
# print("This is the fish list->", fish)
#
# #  school_of_fish ->  |registru de memorie1 [.......]
# #  fish -> |registru de memorie2 [.......]

# school_of_fish = ["crap", "salau", "mreana","somn","somn","somn","salau"]
# school_of_fish.insert(2, "clean")
# print(school_of_fish)
# school_of_fish.reverse()
# #print(school_of_fish)
# #school_of_fish.remove("crap")
# school_of_fish.remove("salau")
# print(school_of_fish)
# school_of_fish.sort()
# print(school_of_fish)
# school_of_fish.sort()
# school_of_fish.reverse()
# print(school_of_fish)

# Tuple
# indexabil
# imutabil
# eterogen

# fish = ("nisetru", "rechin", "merluciu")
# fish = list(fish)
# fish.append("dorada")
# fish = tuple(fish)
# print(fish, type(fish))

# Set
# mutabil
# neidaxbil
# neordonat
# Fara elemente dublicat

# a = {2, 1, 5, 3, 5, 4} # -> {1,2,3,4,5}
# farming = { "rosii", "castraveti", "rosii", "capsuni" }
# print(a)

# Operatiile cu multimi
# A = {1,2,3}
# B = {2,3,4}
# C = {4,5,6}
# A U B = { 1,2,3,4 }
# A n B = {2, 3}
# A - B = {1}
# B - A = {4}
# A - B U B - A
#0 |1 2 3| {4 5 6} 7
# D = {2,3}

# a = []
# b = ()
# c = set()
#
# print(type(a))
# print(type(b))
# print(type(c))

# a = [1]
# b = tuple((1,))
# c = {1}
#
# print(type(a))
# print(type(b))
# print(type(c))

# genres = ["drama", "comedy", "thriller", "horror", "action"]
# movies = ["Schindler's List", "Hangover", "Psycho", "The shining", "Lethal Weapon"]
#
# print("In genul", genres[0], "se incadreaza filmul", movies[0])

movies_by_Genre = {"drama": "Schindler's List",
                   "comedy": "Hangover",
                   "thriller": "Psycho",
                   "horror": "The shining",
                   "action": "Lethal Weapon"}

#print(movies_by_Genre, type(movies_by_Genre))
# movie_details = { "title": "Openheimer",
#                   "cast": [ "Cilian Murphy", "Robert Downey Junior", "Matt Damon" ],
#                   "director": "Cristopher Nolan",
#                   "production_year": 2023,
#                   "release_year": 2023
#                 }

# categ = list(movie_details.keys())
# print(categ)
# print(type(categ))

# details = list(movie_details.values())
# print(details)
# print(type(details))

# categ_details = list(movie_details.items())
# print(categ_details)
# print(type(categ_details))
# movie_details["length"] = 180
# print(movie_details)

# movie_details = { "title": "Openheimer",
#                   "cast": [ "Cilian Murphy", "Robert Downey Junior", "Matt Damon" ],
#                   "director": "Cristopher Nolan",
#                   "production_year": 2023,
#                   "release_year": 2023
#                 }

# Secventa decizionala (if/elif/else)

# data = input("Introduceti titlul, regizorul sau anul de productie:")

# if data.upper() == movie_details["title"].upper():
#     print("Am gasit filmul")
#     print("Incepe proiectia")
# elif data.upper() == movie_details["director"].upper():
#     print("Avem pe stoc un film regizat de", movie_details["director"])
#     print("Urmeaza sa proiectam", movie_details["title"])
# elif str(movie_details["production_year"]) in data:
#     print("Am gasit un film din anul dorit:")
#     print("Urmeaza sa proiectam", movie_details["title"])
# else:
#     print("Filmul nu este in lista in aceasta seara")
#     print("Film disponibil:", movie_details["title"])


# if (data.upper() == movie_details["title"].upper()
#         or data.upper() == movie_details["director"].upper()
#         or str(movie_details["production_year"]) in data):
#     print("Filmul a fost detectat")
# else:
#     print("Nu avem un film care sa indeplineasca toate criteriile")
#
# print("End")

# Structura cu un numar necunoscut de repetari

# lower_limit = input("Introduceti limita de jos:")
# upper_limit = input("Introduceti limita de sus:")
# lower_limit = int(lower_limit)
# upper_limit = int(upper_limit)
#
# while upper_limit >= lower_limit:
#     if upper_limit % 2 == 0:
#         print(upper_limit)
#     upper_limit -= 1
# print("End")

# option = "yes"
#
# movie_details = {"title": "Openheimer",
#                  "cast": ["Cilian Murphy", "Robert Downey Junior", "Matt Damon"],
#                  "director": "Cristopher Nolan",
#                  "production_year": 2023,
#                  "release_year": 2023
#                  }
#
# while option == "yes":
#
#     title = input("Introduceti titlul dorit:")
#
#     if title.upper() == movie_details["title"].upper():
#         print("Filmul va incepe!")
#     else:
#         print("Filmul nu este pe stoc!")
#     option = input("Doriti sa continuati?(yes/no)")

# while True:
#     print("I won t stop ever!!!!!Muhahaha!!!")

movie_details = {"title": "Openheimer",
                 "cast": ["Cilian Murphy", "Robert Downey Junior", "Matt Damon"],
                 "director": "Cristopher Nolan",
                 "production_year": 2023,
                 "release_year": 2023
                 }

# while True:
#
#     title = input("Introduceti titlul dorit:")
#     if title.upper() == "BARBIE":
#         print("Nu permitem aceasta optiune...reluam")
#         continue
#     elif title.upper() == movie_details["title"].upper():
#         print("Filmul va incepe!")
#
#     else:
#         print("Filmul nu este pe stoc!")
#     option = input("Doriti sa continuati?(yes/no)")
#     if option == "no":
#         break

# a = [ "omleta", "zacusca", "parizer", "pizza" ]
# b = [ "Florin", "Oana", "Sebi", "Beatrice" ]
#
# for item in b:
#     print(item)

# food = "shaorma"
#
# for item in food:
#     print(item)
#

# immutable_food = ( "mbs", "carbonarra", "lasagna" )
#
# for food in immutable_food:
#     print(food)


# for ( i=5; i<= 34; i= i+5 )

# print(range(10), type(range(10)))

# Cerem input de la utilizator -> check
# Parcurgem intervalul -> check
# Verific daca numarul este impar


# a = int(input("Introduceti numarul inferior:"))
# b = int(input("Introduceti numarul superior:"))
#
# for item in range(a, b + 1): # -> [ 0, 1,..................101]
#     if item % 2 != 0:
#         print(item)

# for i in range(10, 1, -1):
#     print(i)


# a = [ "omleta", "zacusca", "lapte cu cereale" ,"parizer", "pizza" ]
# b = [ "Florin", "Oana", "Vlad" ,"Sebi", "Beatrice" ]

# for item in range(len(a)):
#     if a[item] == "lapte cu cereale":
#         print("S a cerut lapte cu cereale...posibila intoleranta la lactoza...aborting")
#         break
#     message = f'{b[item]} prefera {a[item]}'
#     print(message)

# for item in range(len(a)):
#     if a[item] == "lapte cu cereale":
#         print("S a cerut lapte cu cereale...posibila intoleranta la lactoza...skipping")
#         continue
#     message = f'{b[item]} prefera {a[item]}'
#     print(message)

# a = [ "omleta",
#       "zacusca",
#       "lapte cu cereale",
#       "parizer",
#       "pizza" ]
#
#
# b = [ "Florin", "Oana", "Vlad" ,"Sebi", "Beatrice" ]
#
# f = input("Ce fel de mancare doriti sa identiicam?")
#
# food_dict = { "Florin": "omleta",
#               "Oana": "zacusca",
#               "Vlad": "lapte cu cereale",
#               "Sebi" : "parizer",
#               "Beatrice": "pizza",
#               "Mihail": "parizer"
#             }
#
# c = list(food_dict.keys())
# d = list(food_dict.values())
#
# for item in range(len(c)):
#     if d[item] == f:
#         print(c[item])


# Sa se verifice daca un numar introdus de la tastura este sau nu palindrom

## Metoda clasica

### Cerem numar -> check
#### Sa i calculez invers -> check
###### Comparam numarul initial cu inversul
####### Afisam mesaj corespunzator

# numar_initial = int(input("Va rog introduceti numarul:"))
# numar = numar_initial
# invers = 0
#
#
# while numar_initial != 0:
#     invers = invers * 10 + numar_initial % 10
#     numar_initial = numar_initial // 10
#
#
# if numar == invers:
#     print("Numarul este palindrom!")
# else:
#     print("Numarul nu este palindrom")


#Explicatie

#### nr_initial = 123, invers = 0 -> 123 !=0? -> DA -> invers = 0 * 10 + 123 % 10 = 0 + 3=3
#                                                      numar_initial = 123 // 10 = 12
### invers = 3, numar_initial= 12 -> 12 ! = 0? -> DA -> invers= 3 * 10 + 12 % 10 = 30 + 2 = 32
#                                                       numar_initial = 12 // 10 = 1
##  invers = 32, numar_initial = 1 1 != 0 -> DA invers = 32 * 10 + 1 % 10 = 320 + 1 = 321
#                                               numar_initial = 1 //10 = 0
# invers = 321, numar_initial=0  0 !=0? -> NU


## Metoda python

numar_initial = input("Va rog introduceti numarul:")

if numar_initial == numar_initial[::-1]:
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")