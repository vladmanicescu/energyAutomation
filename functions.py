# f(x) = x + 1
# f(1) = 1 + 1 = 2
# f(x,y) = x + y
# f(2,3) = 2 + 3 = 5

# def nume_functie(params):
#      """Docstring"""
#      corpul_functiei(instructiunile)
#      return

def greetings():
    """
     Simple academic greetings function.
     Prints out a greeting message
    :return: None
    """
    return "Hello world!"

def specific_greetings(name, age):
    """
    Simple academic specific greetings funtion. Prints out a greetings message
    :param name: str Name of the person to be greeted
    :param age: int Age of the person to be greeted
    :return: None
    """
    greeting = f"Hello {name}!"
    info = f"You are {age} years old!"
    print(greeting)
    print(info)

def custom_sum(a, b):
    """
    Function that computes the sum of two numbers
    :param a: int
    :param b: int
    :return: int
    """
    result = a + b
    return result

def ispalindrome(n):
    """
    Function that returns whether or not an argument is palindrome
    :param n: int
    :return: bool
    """
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

# greetings()
# specific_greetings("Sebastian", 23)
# print(specific_greetings("Vlad", 104))
#specific_greetings("Vlad", 104)
# c = custom_sum(3,5)/2
# print(c)
def main():
    # print("Hello")
    # print(custom_sum(3, 6) / 2)
    # print("This is functions name", __name__)
    print(ispalindrome(203))



if __name__ == "__main__":
    main()

