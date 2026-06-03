# Exercise 1 – Student Grades (Lists + Flow Control)
#
# grades = [7, 10, 9, 5, 8, 4, 10]
#
# Tasks: 1. Calculate the average grade. 2. Count how many grades are
# passing (>= 5). 3. Count how many grades are failing (< 5). 4. Print the
# highest and lowest grade. 5. Print all grades greater than the average.
from operator import countOf

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
