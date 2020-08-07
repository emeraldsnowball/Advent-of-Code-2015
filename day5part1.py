from sys import argv

script, input_file = argv

open_file = open(input_file)
txt = open_file.read().split()
nice_string = []
for line in txt:
    count_vowel = 0
    double_letter = 0

    if 'ab' in line:
        continue
    if 'cd' in line:
        continue
    if 'pq' in line:
        continue
    if 'xy' in line:
        continue

    count_vowel += line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')

    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            double_letter += 1

    if count_vowel >= 3 and double_letter >= 1:
        nice_string.append(line)

print("part 1:", len(nice_string))
