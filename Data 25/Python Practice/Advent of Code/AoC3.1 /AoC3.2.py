def power_consumption(file):
    with open("binary.txt", 'r') as binary_file:
        binary_list = binary_file.readlines()
        oxygen_generator = []
        CO2_scrubber = []
        for x in range(0, 12):
            count_of_0 = 0
            count_of_1 = 0
            for row in binary_list:
                if row[x] == "0":
                    count_of_0 += 1
                else:
                    count_of_1 += 1
            if count_of_0 > count_of_1:


        for i in oxygen_generator:
            if i == 0:
                CO2_scrubber.append(1)
            else:
                CO2_scrubber.append(0)
        print(oxygen_generator)
        print(len(oxygen_generator))
        print(CO2_scrubber)


power_consumption("binary.txt")