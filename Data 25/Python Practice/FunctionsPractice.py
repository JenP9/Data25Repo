print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:


def func1(integer):
    divisors = []
    for i in range(1, integer+1):
        if integer % i == 0:
            divisors += [i]
    return divisors


print(func1(64))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:


def func2(int1, int2):
    if int1 % int2 ==0:
        print("True.")
    elif int2 % int1 ==0:
        print("True.")
    else:
        print("False.")


func2(5, 10)


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:


def func3(letter):
    print(alphabet.index(letter) +1 )


func3('j')


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def func4(name):
    id_number = ""
    for letter in name:
        id_number += str(alphabet.index(letter))
    return id_number


print(func4('bob'))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:


def func5(id_number):
    sum = 0
    for i in id_number:
        sum += int(i)
    return int(id_number) - sum


print(func5('1141'))




# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:


def func6(num):
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 9:
        print("True")
    elif num%1 == 0 and num%num == 0 and num%2 != 0 and num%3 != 0 and num%5 != 0 and num%7 != 0 and num%9 != 0:
        print("True.")
    else:
        print("False.")
# This is a long way around it I know how to do the simpler way now

func6(44)

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:


def func7(num):
    if type(num) == int:
        func6(num)
    else:
        print("Error.")


func7(44)

# -------------------------------------------------------------------------------------- #






