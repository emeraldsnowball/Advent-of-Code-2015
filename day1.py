from sys import argv

sript, input_file = argv

open_file = open(input_file)
content = open_file.read()

print("part 1:",content.count('(') - content.count(')'))
count = 0
i = 0
for a in content:
    i+=1
    if a == '(':
        count = count + 1
    elif a == ')':
        count = count - 1
    if count == -1:
        print("part 2:", i)
        break
