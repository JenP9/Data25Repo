def counter(file):
    with (open("measurements.txt", "r")) as measurement_file:
        measurement_list = measurement_file.readlines()
        list_of_measurements = []
        for num in measurement_list:
            list_of_measurements.append(int(num))
        count = 0
        for i in range(1, len(list_of_measurements)):
            if list_of_measurements[i-1] < list_of_measurements[i]:
                count += 1
        return count


print(counter("measurements.txt"))