from sys import argv

script, input_file = argv

open_file = open(input_file)
directions = open_file.read()

houses = [(0,0)]
i = 0
for d in directions:
    if d == '^':
        houses.append([houses[i][0]+1, houses[i][1]])
    if d == 'v':
        houses.append([houses[i][0]-1, houses[i][1]])
    if d == '>':
        houses.append([houses[i][0], houses[i][1]+1])
    if d == '<':
        houses.append([houses[i][0], houses[i][1]-1])
    i += 1

unique_house = []

for house in houses:
    if house not in unique_house:
        unique_house.append(house)

print("part 1:", len(unique_house))
