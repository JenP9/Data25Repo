def valid_passwords(password_list):

    with open(password_list, 'r') as passwords:
        passwords_list = passwords.readlines()
        counter = 0
        list = []
        valid = 0
        for row in passwords_list:
            list.append(row)

        for x in list:
            range = x.split()[0]
            minimum = int(range.split("-")[0])
            maximum = int(range.split("-")[1])
            letter_1 = x.split()[1]
            letter = letter_1.split(":")[0]
            combination = x.split(":")[1]
            for y in combination:
                counter = 0
                if y == letter:
                    counter += 1
                else:
                    pass
                if minimum <= counter <= maximum:
                    valid += 1
                else:
                    pass
        print(valid)


valid_passwords("passwords.txt")