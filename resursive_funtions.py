# Functii recursive
# 0! = 1
# 1! = 1
# 2! = 1 * 2 = 2
# 3! = 1 * 2 * 3 = 6
# 4! = 1 * 2 * 3 * 4 = 24
# 5! = 1*2 *3 *4 *5 = 120
# 6! = 1*2 *3 *4 *5* 6 = 720 = 5! * 6

import sys
def user_input()-> int:
    """

    :return:
    """
    try:
        a = int(input("Introduceti numarul:"))
        if a == 0:
            raise ValueError("ZeroValueError")
    except ValueError:
        print("Va rog introduceti numere naturale!!!")
        sys.exit(5)
    except RecursionError:
        print("Va rog introduceti numere naturale pozitive!!!")
        sys.exit(5)
    return a

def iterative_factorial(n: int)-> int:
    """

    :param n:
    :return:
    """
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def recursive_factorial(n: int)-> int:
       if n == 1:
           return 1
       else:
           print(n)
           return n * recursive_factorial(n - 1)



# n = 4 -> 4 == 1? NO -> 4 * 3 *  2 * 1
#                            3 == 1? -> NO 3 * rec_fac(2)
#                                              2 == 1? -> NO -> 2 * rec_fac(1)
#                                                                    1 == 1? -> YES -> 1

def main():
    option = user_input()
    print(recursive_factorial(option))
    print("Continua algoritmul")



if __name__ == "__main__":
    main()