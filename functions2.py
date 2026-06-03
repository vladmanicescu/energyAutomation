# Program care sa ceara utilizatorului doua numere si sa puna intr o lista toate numerele pare dintre numerele date de utilizator.
# Programul sa intoarca lista de numere si , lista cu patratul numerelor pare e.g
#[2,4,8] -> [4,16,64]
# Inputul utilizatorului se cere printr o functie
# Numerele pare sunt determinate intr o functie

def in_user()-> tuple:
    """
    Takes info from user
    :return: tuple of numbers the user gave e.g (2, 11)
    """
    a = int(input("Introduceti limita inferioara[nr intreg pozitiv]:"))
    b = int(input("Introduceti limita superioara[nr intreg pozitiv]:"))
    return a,b

def numbers(a: int, b: int)-> tuple:
    """
     Returns list of even numbers in an interval and a list squares of the elements of the first list
    :param a: int
    :param b: int
    :return: Return of one list of even numbers between the two, and another list of the squared values in the
    first list
    """
    # list_of_even_numbers = []
    # list_of_squared_even_numbers = []
    # for i in range(a, b+1):
    #     if i % 2 == 0:
    #         list_of_even_numbers.append(i)
    #         list_of_squared_even_numbers.append(i**2)
    #
    # List comprehension style
    # A = {x, x e N || x divizibil 3 } } -> A = {3,9}
    list_of_even_numbers = [ i for i in range(a, b+1) if i % 2 == 0]
    list_of_squared_even_numbers = [ i**2 for i in list_of_even_numbers]
    return list_of_even_numbers, list_of_squared_even_numbers

def main()-> None:
    """
    Main function of the program
    :return: None
    """
    user_input_1, user_input_2 = in_user()
    print(numbers(user_input_1, user_input_2))




if __name__ == "__main__":
    main()