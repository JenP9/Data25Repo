def counter(file):
    with (open("measurements.txt", "r")) as measurement_file:
        measurement_list = measurement_file.readlines()
        list_of_measurements = []
        for num in measurement_list:
            list_of_measurements.append(int(num))
        count = 0
        for i in range(1, len(list_of_measurements)-2):
            total1 = list_of_measurements[i] + list_of_measurements[i-1] + list_of_measurements[i+1]
            total2 = list_of_measurements[i] + list_of_measurements[i+1] + list_of_measurements[i+2]
            if total1 < total2:
                count += 1
        return count


print(counter("measurements.txt"))