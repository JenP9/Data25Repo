def power_consumption(file):
    with open("binary.txt", 'r') as binary_file:
        binary_list = binary_file.readlines()
        gamma_rate = []
        epsilon_rate = []
        for x in range(0, 12):
            count_of_0 = 0
            count_of_1 = 0
            for row in binary_list:
                if row[x] == "0":
                    count_of_0 += 1
                else:
                    count_of_1 += 1
            if count_of_0 > count_of_1:
                gamma_rate.append(0)
            else:
                gamma_rate.append(1)

        for i in gamma_rate:
            if i == 0:
                epsilon_rate.append(1)
            else:
                epsilon_rate.append(0)

        gamma_rate = ''.join(str(i) for i in gamma_rate)
        epsilon_rate = ''.join(str(i) for i in epsilon_rate)
        print(gamma_rate)
        print(epsilon_rate)
        print(2277*1818)

power_consumption("binary.txt")