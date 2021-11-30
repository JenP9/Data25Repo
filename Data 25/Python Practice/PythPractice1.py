print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
list1 = []
for i in range(0, 5):
    list1 += [x[i]]

print(list1)


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
list2 = []
for i in x:
    if i%2 == 0:
        list2 += [i]

print(list2)

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
list3 = []
for i in range(0, 5):
    if x[i]%2 == 0:
        list3 += [x[i]]

print(list3)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
list4 = []
for people in names:
    list4 += (people[0])

print(list4)


print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
list5 = []
for substrings in names:
    index1 = substrings.index(' ')
    list5 += [index1]

print(list5)


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
list6 = []
for substrings in names:
    index1 = substrings.index(' ')
    list6 += [substrings[0]+substrings[index1+1]]

print(list6)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1, 5, 7, 3, 44, 4, 1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
for lists in list_of_lists:
    print(set(lists))


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
number = int(input('Enter a number greater than 100: '))
while number < 100:
    number = int(input('Enter another number greater than 100: '))

print(number)


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
number = int(input('Enter a number greater than 100: '))
while number < 100:
    number = int(input('Enter another number greater than 100: '))
if number > 1:
    prime = False
    for i in range(2, number):
        if (number % i) == 0:
            prime = True
        else:
            prime = False
if prime is True:
    print("prime")
else:
    print("not prime")
print(number)








