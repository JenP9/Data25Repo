def debug(file):
    with (open("passwords.txt", "r")) as password_file:
        x = 0
        for i in password_file:
            policy, password = [item.strip() for item in i.split(':')]
            letter = policy[-1]
            ind1, ind2 = [int(j) for j in policy[:-2].split('-')]
            ind1 = ind1 - 1
            ind2 = ind2 - 1

            if password[ind1] == letter and password[ind2] == letter:
                pass
            elif password[ind1] == letter or password[ind2] == letter:
                x += 1
        print(x)


debug("passwords.txt")