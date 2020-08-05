from sys import argv

script, input_file = argv

open_file = open(input_file)
directions = open_file.read()
houses = [(0,0)]
robot_houses = [(0,0)]
i = 0
for d in directions:
    if i%2 == 0:
        if d == '^':
            houses.append([houses[len(houses) - 1][0]+1, houses[len(houses) - 1][1]])
        elif d == 'v':
            houses.append([houses[len(houses) - 1][0]-1, houses[len(houses) - 1][1]])
        elif d == '>':
            houses.append([houses[len(houses) - 1][0], houses[len(houses) - 1][1]+1])
        elif d == '<':
            houses.append([houses[len(houses) - 1][0], houses[len(houses) - 1][1]-1])
    else:
        if d == '^':
            robot_houses.append([robot_houses[len(robot_houses) - 1][0]+1, robot_houses[len(robot_houses) - 1][1]])
        elif d == 'v':
            robot_houses.append([robot_houses[len(robot_houses) - 1][0]-1, robot_houses[len(robot_houses) - 1][1]])
        elif d == '>':
            robot_houses.append([robot_houses[len(robot_houses) - 1][0], robot_houses[len(robot_houses) - 1][1]+1])
        elif d == '<':
            robot_houses.append([robot_houses[len(robot_houses) - 1][0], robot_houses[len(robot_houses) - 1][1]-1])
    i += 1

unique_house = []

for house in robot_houses:
    if house not in unique_house:
        unique_house.append(house)

for house in houses:
    if house not in unique_house:
        unique_house.append(house)
print("part 2:", len(unique_house))
