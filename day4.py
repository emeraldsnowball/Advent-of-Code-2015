from hashlib import md5

for i in range(10000000):
    input = 'iwrupvqb' + str(i)
    hash = md5((input).encode()).hexdigest()
    if hash[:5] == '00000':
        print("part 1:",i)
        break

for i in range(1000000, 1000000000):
    input = 'iwrupvqb' + str(i)
    hash = md5((input).encode()).hexdigest()
    if hash[:6] == '000000':
        print("part 2:",i)
        break
