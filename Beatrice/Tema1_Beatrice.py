"""Exercițiul 1: Schimb Valutar Interactiv
Cere utilizatorului o sumă în RON (număr întreg sau zecimal). Calculează valoarea în EUR folosind un curs fix de 4.97 și afișează rezultatul.

Exercițiul 2: Dinamic String Slicing
Cere utilizatorului să introducă un cuvânt la alegere. Extrage și afișează prima și ultima literă folosind indexarea.

Exercițiul 3: Construirea unei liste de cumpărături
Cere utilizatorului să introducă pe rând 3 produse pe care vrea să le cumpere. Salvează-le direct într-o listă și afișează lista finală.

Exercițiul 4: Modificarea listei prin index ales
Ai lista orase = ["București", "Cluj", "Timișoara"]. Cere utilizatorului un oraș nou și numărul indexului pe care vrea să îl înlocuiască (0, 1 sau 2). Executa inlocuirea.

Exercițiul 5: Coada de așteptare
Ai o listă inițială cu clienți: coada = ["Elena", "Andrei"]. Cere utilizatorului numele unui client nou. Adaugă-l la sfârșitul listei folosind și afișează noua lungime a listei.

Exercițiul 6: Eliminare din listă
Ai o listă de sarcini: taskuri = ["Curățenie", "Cumpărături", "Teme"]. Cere utilizatorului să specifice  sarcinia pe care a finalizat-o (0, 1 sau 2). Șterge acea sarcină din listă folosind și afișează elementul care a fost eliminat."""
import re

"""Rezolvari"""

#Exercitiul 1:
suma_ceruta = float(input("Mentionati o suma in RON: ")) #convertim din str in float pt. op. matematice
valoare_euro = 4.97

print([suma_ceruta, type(suma_ceruta)], [valoare_euro, type(valoare_euro)])
print("Valoarea in EUR este:", suma_ceruta / (valoare_euro))

#Exercitiul 2:
cuvant_utilizator = input("Introduceti un cuvant la alegere: ")
print("Prima litera este: ",(cuvant_utilizator)[0],", iar ultima litera este: ",(cuvant_utilizator)[-1])

#Exercitiul 3:
lista_cumparaturi = input("Introduceti 3 produse pe care doriti sa le cumparati la urmatoarea vizita intr-un magazin: ")
list([lista_cumparaturi])

print("Lista finala de cumparaturi este: ",list([lista_cumparaturi]))

#Exercitiul 4:
lista_orase = ["București", "Cluj", "Timișoara"]
print("Lista initiala de orase este: ",lista_orase)

oras_nou = input("Mentionati alt oras in afara listei: ".format(lista_orase))
print(oras_nou)
#oras_nou = input("Mentionati alt oras in afara listei: {}. ".format(lista_orase)) ---- cum afiseaza lista {} ?

index_de_inlocuit = int(input("Ce index doriti sa fie inlocuit din lista initiala (0, 1 sau 2): "))

while index_de_inlocuit not in [0, 1, 2]:
    index_de_inlocuit = int(input("Index invalid. Introduceti un index valid (0, 1 sau 2): "))

#oras_nou = lista_orase[index_de_inlocuit] # de ce nu merge si asta, nu arata ca cea de jos?
lista_orase[index_de_inlocuit] = oras_nou
print("Lista actualizata de orase este: ", lista_orase)

#Exercitiul 5:
coada = ["Elena", "Andrei"]
nume_client_nou = input("Adaugati un prenume de client nou: ")
nume_client_nou = [nume_client_nou]
print(nume_client_nou, type(nume_client_nou),coada, type(coada))

coada = coada + nume_client_nou
print(coada)

#noua_coada = coada.append(nume_client_nou)
#print("Cu append ar fi: ", coada, noua_coada)

#Exercitiul 6:
taskuri = ["Curățenie", "Cumpărături", "Teme"]
sarcina_finalizata = int(input("Specifica index-ul task-ului finalizat (0, 1 sau 2): "))

if sarcina_finalizata in [0, 1, 2]:
    task_finalizat = taskuri.pop(sarcina_finalizata)
    print(taskuri)

