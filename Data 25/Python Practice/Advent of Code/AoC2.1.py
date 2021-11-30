def debug(file):
    with (open("passwords.txt", "r")) as password_file:
        x = 0
        for i in password_file:
            policy, password = [item.strip() for item in i.split(':')]
            letter = policy[-1]
            mnm, mxm = [int(j) for j in policy[:-2].split('-')]
            count = 0
            for digits in password:
                if digits == letter:
                    count += 1
            if count in range(mnm, mxm+1):
                x += 1
        print(x)


debug("passwords.txt")