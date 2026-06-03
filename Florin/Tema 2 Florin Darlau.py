#Exercise 1 – Student Grades (Lists + Flow Control)
# grades = [7, 10, 9, 5, 8, 4, 10]
# #Avrage grade
# avg_grade=sum(grades)/len(grades)
# print(avg_grade)
# #How many grades are passing (>5)
# passging_grades=0
# falling_grades=0
# for grade in grades:
#     if grade >= 5:
#         passging_grades+=1
#     else:
#         falling_grades+=1
# print(f"Au trecut un numar de {passging_grades}")
# print(f"Au picat un numar de {falling_grades}")
# print(max(grades))
# print(min(grades))
# grades_avrage=[]
# for grade in grades:
#     if grade >= avg_grade:
#         grades_avrage.append(grade)
# print(grades_avrage)
# from http.cookiejar import uppercase_escaped_char
from importlib.resources.readers import remove_duplicates
from multiprocessing.reduction import duplicate
from os import remove

# Exercise 2 – Shopping List (Lists + Loops)

# shopping = ["milk", "bread", "eggs", "milk", "cheese", "bread"]
# print(shopping)
# lista_item=[]
# lista_fara_duplicate=[]
# for item in shopping:
#     if item not in lista_item:
#         lista_item.append(item)
#         print(item, shopping.count(item))
# for item in shopping:
#     if item not in lista_fara_duplicate:
#         lista_fara_duplicate.append(item)
# print (sorted(lista_fara_duplicate))
# input_lista=input("Alegeti un produs sa verificam daca este in lista:")
# input_lista=input_lista.lower()
# if input_lista in shopping:
#     print("Produl este deja in lista")
# else:
#     print("Produsul nu este in lista dar a fost adaugat:")
#     shopping.append(input_lista)
#     print(shopping)




# Exercise 3 – Coordinates (Tuples)
# point = (10, 20)
# coordonata_x=point[0]
# coordonata_y=point[1]
# print(coordonata_x,coordonata_y)
# new_point = (15, 30)
# new_coordonata_x=new_point[0]
# new_coordonata_y=new_point[1]
# distance_x=new_coordonata_x-coordonata_x
# print(distance_x)
# distance_y=new_coordonata_y-coordonata_y
# print(distance_y)
# if coordonata_x>new_coordonata_x:
#     print("Point are coordonata x mai mare")
# else:
#     print("New_Point are coordonata y mai mare")
# points = [(10, 20), (15, 30), (5, 40), (12, 25)]
#
# max_point = points[0]
#
# for point in points:
#     if point[1] > max_point[1]:
#         max_point = point
#
# print("Point with highest y value:", max_point)




# Exercise 4 – Employee Database (Dictionaries)

# employee = {"name": "John", "age": 30, "department": "IT", "salary": 5000}
# print(employee.keys())
# print(employee.values())
# employee["salary"] = employee["salary"]*1.10
# print(employee)
# employee["city"]="Brasov"
# if "manager" in employee:
#     print("Manager exsita")
# else:
#     print("Manager nu exsita")




# Exercise 5 – Unique Visitors (Sets)

# visitors = [101, 102, 103, 101, 104, 102, 105]
# visitors_set=set(visitors)
# print(visitors_set)
# print(len(visitors_set))
# if 103 in visitors_set:
#     print("103 exista")
# else:
#     print("103 nu exista")
# visitors_set.add(106)
# print(visitors_set)
# visitors_set.remove(101)
# print(visitors_set)


# Exercise 6 – Inventory Manager (Dictionary + Flow Control)

# inventory = { "apple": 10, "banana": 5, "orange": 8 }
# for product, quantity in inventory.items():
#     print(f"{product} sunt {quantity}")
# q_bellow_6=[]
# for product, quantity in inventory.items():
#     if quantity > 6:
#         q_bellow_6.append(product)
# print(q_bellow_6)
# product_name = input("Introdu numele produsului dorit:")
# product_name=product_name.lower()
# if product_name in inventory:
#     print("Cantitatea:", inventory[product_name])
# else:
#     print("Produsul nu este in lista")




# Exercise 7 – Common Interests (Sets

# alice = {"reading", "gaming", "swimming"}
# bob = {"gaming", "cooking", "swimming"}
# print(alice.intersection(bob))
# print(alice.difference(bob))
# print(bob.difference(alice))
# print(alice.union(bob))

# Exercise 8 – Student Registry (List + Dictionary)

# students = [
#     {"name": "Ana", "grade": 8},
#     {"name": "John", "grade": 10},
#     {"name": "Maria", "grade": 6},
#     {"name": "Alex", "grade": 4}
# ]
# for student in students:
#     print(student["name"])
#
# s_highesr_grade =students[0]
# for student in students:
#     if student["grade"] > s_highesr_grade["grade"]:
#         s_highesr_grade = student
# print(s_highesr_grade)
#
# total=0
# for student in students:
#     total = total + student["grade"]
# avrage = total/len(students)
# print(avrage)
# for student in students:
#     if student["grade"] >= 5:
#         print(f"studentii care au trecut sunt: {student["name"]}")
# for student in students:
#     if student["grade"] >= avrage:
#         print(f"studentii care au nota mai mare decat media clasei: {student["name"]}")


# Exercise 9 – Movie Collection (Tuple + Dictionary)

# movies = {
#     "Inception": (2010, 8.8),
#     "Interstellar": (2014, 8.6),
#     "The Matrix": (1999, 8.7)
# }
# for movie, details in movies.items():
#     print(movie, details)
# highest_rating = 0
# for movie, details in movies.items():
#     if details[1] > highest_rating:
#         highest_rating = details[1]
#         print(f"filmul cu cel mai bun rating este {movie,details}")
# for movie, details in movies.items():
#     if details[0] > 2005:
#         print("Filmele mai noi de 2005", movie)
# total_rating = 0
#
# for movie, details in movies.items():
#     total_rating += details[1]
#
# average_rating = total_rating / len(movies)
# print("Average rating:", average_rating)

# Exercise 10 – Number Analyzer (Everything Together)
# numbers = [3, 7, 2, 7, 9, 2, 10, 3, 8]
# numbers_set=set(numbers)
# remove_duplicates(numbers_set)
# print(numbers_set)
# numbers_set = list(numbers_set)
# numbers_set.sort()
# print(numbers_set)
#
# numbers_dictionar={}
# for number in numbers_set:
#     if number % 2 == 0:
#         numbers_dictionar[number] = "even"
#     else:
#         numbers_dictionar[number] = "odd"
# print(numbers_dictionar)
#
# for number in numbers_set:
#     if numbers_dictionar == "even":
#         print(f"Numerele pare sunt{number}")
#     else:
#         print(f"Numerele impare sunt{number}")
# min_max = (numbers_list[0], numbers_list[-1])
# print(min_max)