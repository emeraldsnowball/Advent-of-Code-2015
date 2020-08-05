from sys import argv

sript, input_file = argv

open_file = open(input_file)
content = open_file.read().split()

boxes = []

for i in content:
    boxes.append(i.split('x'))
i = 0
for box in boxes:
    boxes[i] = [int(j) for j in box]
    i += 1

wrapping = 0
ribbon = 0
for box in boxes:
    wrapping += 2*box[0]*box[1] + 2*box[1]*box[2] + 2*box[2]*box[0]
    wrapping += sorted(box)[0]*sorted(box)[1]
    ribbon += box[0]*box[1]*box[2] + 2 * (sorted(box)[0] + sorted(box)[1])

print("part 1:", wrapping)
print("part 2:", ribbon)
