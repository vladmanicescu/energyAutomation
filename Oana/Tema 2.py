# Exercise 1 – Student Grades (Lists + Flow Control)
#
# grades = [7, 10, 9, 5, 8, 4, 10]
#
# Tasks: 1. Calculate the average grade. 2. Count how many grades are
# passing (>= 5). 3. Count how many grades are failing (< 5). 4. Print the
# highest and lowest grade. 5. Print all grades greater than the average.
from email import message

print("Exercitiul 1")
grades = [7, 10, 9, 5, 8, 4, 10]
average = round(sum(grades) / len(grades),2)
print("Media notelor este: " + str(average))
big_grades = []
small_grades = []
for gr in grades:
    if gr >= 5:
        big_grades.append(gr)
    else:
        small_grades.append(gr)
print(big_grades)
print(small_grades)
print("Nr notelor peste 5 este: "+str(len(big_grades)))
print("Nr notelor sub 5 este: " + str(len(small_grades)))
#print(grades.sort())  --- de ce nu merge asta?
grades.sort()
print("lista sortata este: ",grades)
print("Cel mai mic nr este: ",grades[0])
print("Cel mai mare nr este: ",grades[-1])
big_avg = []
for ba in grades:
    if ba >average:
        big_avg.append(ba)
print("Nr peste medie sunt: ",big_avg)

# Exercise 2 – Shopping List (Lists + Loops)
#
# shopping = [“milk”, “bread”, “eggs”, “milk”, “cheese”, “bread”]
#
# Tasks: 1. Print all items. 2. Count how many times each item appears. 3.
# Remove duplicates. 4. Sort the list alphabetically. 5. Ask the user for
# an item and check if it exists in the list.

print("----------------------------")
print("Exercitiul 2")
shopping = ['milk', 'bread', 'eggs', 'milk', 'cheese', 'bread']
print ("Lista de cumparaturi este: ",shopping)
x=dict((i, shopping.count(i)) for i in shopping)
print ("De cate ori apare fiecare element?: ",x)
zero_duplicate = []
for i in shopping:
    if i not in zero_duplicate:
        zero_duplicate.append(i)
print("Lista sortata fara duplicate: ",sorted(zero_duplicate))
inp_user=input("Ce ingredient cautati? ")
for i in zero_duplicate:
    if i==inp_user:
        print ("Ingredientul",inp_user,"apare in lista")
        break
    if i!=inp_user:
        print("Ingredientul", inp_user, "nu apare in lista")
        break


