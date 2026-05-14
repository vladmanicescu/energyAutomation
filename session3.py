from audioop import reverse

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

a = [1]
b = tuple((1,))
c = {1}

print(type(a))
print(type(b))
print(type(c))