from sys import argv

script, input_file = argv

open_file = open(input_file)
txt = open_file.read().split()
nice_string = []
for line in txt:
    count_two_letter = 0
    double_letter_sep = 0

    for i in range(len(line)-1):
        if line.count(line[i] + line[i+1]) >= 2:
            count_two_letter += 1

    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            double_letter_sep += 1

    if count_two_letter >= 1 and double_letter_sep >= 1:
        nice_string.append(line)

print("part 2:", len(nice_string))
