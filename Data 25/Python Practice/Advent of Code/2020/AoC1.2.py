import random


def expenses(file):
    with (open("expense_report.txt", "r")) as expense_file:
        expense_list = expense_file.readlines()
        list_of_nums = []
        for num in expense_list:
            list_of_nums.append(int(num))

        total_is_2020 = False
        while total_is_2020 is False:
            random_value1 = random.randint(0, len(list_of_nums)-1)
            random_value2 = random.randint(0, len(list_of_nums)-1)
            random_value3 = random.randint(0, len(list_of_nums)-1)
            rand_from_list1 = list_of_nums[random_value1]
            rand_from_list2 = list_of_nums[random_value2]
            rand_from_list3 = list_of_nums[random_value3]
            if rand_from_list1 + rand_from_list2 + rand_from_list3 == 2020:
                print(rand_from_list1)
                print(rand_from_list2)
                print(rand_from_list3)
                print(rand_from_list1 * rand_from_list2 * rand_from_list3)
                total_is_2020 = True


expenses("expense_report.txt")
