def move_sub(file):
    with open('commands.txt', 'r') as commands:
        directions = commands.readlines()
        list_of_directions = []

        for n in directions:
            list_of_directions.append(n)

        horizontal = 0
        depth = 0
        for n in list_of_directions:
            if n.split(' ')[0] == "forward":
                horizontal += int(n.split(' ')[1])
            elif n.split(' ')[0] == "down":
                depth += int(n.split(' ')[1])
            elif n.split(' ')[0] == "up":
                depth -= int(n.split(' ')[1])
        print(horizontal)
        print(depth)
        print(horizontal * depth)


move_sub("commands.txt")