# Exercițiul 1: Schimb Valutar Interactiv
# Cere utilizatorului o sumă în RON (număr întreg sau zecimal). Calculează valoarea în EUR folosind un curs fix de 4.97 și afișează rezultatul.
#
# Exercițiul 2: Dinamic String Slicing
# Cere utilizatorului să introducă un cuvânt la alegere. Extrage și afișează prima și ultima literă folosind indexarea.
#
# Exercițiul 3: Construirea unei liste de cumpărături
# Cere utilizatorului să introducă pe rând 3 produse pe care vrea să le cumpere. Salvează-le direct într-o listă și afișează lista finală.
#
# Exercițiul 4: Modificarea listei prin index ales
# Ai lista orase = ["București", "Cluj", "Timișoara"]. Cere utilizatorului un oraș nou și numărul indexului pe care vrea să îl înlocuiască (0, 1 sau 2). Executa inlocuirea.
#
# Exercițiul 5: Coada de așteptare
# Ai o listă inițială cu clienți: coada = ["Elena", "Andrei"]. Cere utilizatorului numele unui client nou. Adaugă-l la sfârșitul listei folosind și afișează noua lungime a listei.
#
# Exercițiul 6: Eliminare din listă
# Ai o listă de sarcini: taskuri = ["Curățenie", "Cumpărături", "Teme"]. Cere utilizatorului să specifice  sarcinia pe care a finalizat-o (0, 1 sau 2). Șterge acea sarcină din listă folosind și afișează elementul care a fost eliminat.

#Ex1

print("---EXERCITIUL 1---")
ron = int(input("Introduceti valoarea in RON: "))
print(f"Valoarea introdusa este {ron} RON")
eur = ron * 4.97
print(f"Valoarea in EUR este {eur:.0f}")

print()
print("---EXERCITIUL 2---")
cuv = input("Introduceti cuvantul: ")
p = cuv[0]
u = cuv[-1]
print(f"Prima litera din cuvantul '{cuv}' este '{p}' si ultima este '{u}'")

print()
print("---EXERCITIUL 3---")
lista = []
for i in range(3):
    produs = input(f"Introduceti produsul {i + 1}: ")
    lista.append(produs)
print(f"Lista finala de produse este: {lista}")

print()
print("---EXERCITIUL 4---")
orase = ["București", "Cluj", "Timișoara"]
oras_nou = input("Introduceti orasul dorit: ")
index = int(input("Introduceti indexul dorit (0, 1, 2): "))
print(f"Orasele inainte de inlocuire: {orase}")
orase[index] = oras_nou
print(f"Orasele dupa inlocuire: {orase}")

print()
print("---EXERCITIUL 5---")
coada = ["Elena", "Andrei"]
nume_nou = input("Introduceti un nume nou: ")
coada.append(nume_nou)
print(f"Lista de nume este: {coada}, iar lungimea este '{len(coada)}'")

print()
print("---EXERCITIUL 6---")
taskuri = ["Curățenie", "Cumpărături", "Teme"]
print(f"Lista de taskuri este: {taskuri}")
index = int(input("Introduceti index-ul taskului de eliminat (0, 1, 2): "))
task_vechi = taskuri[index]
taskuri.remove(task_vechi)
print(f"Lista dupa eliminarea taskului '{task_vechi}', este: {taskuri}")