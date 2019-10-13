with open ('file.txt', 'w') as inf:
    inf.write('some text \n')
    inf.write(str(25))

with open ('file.txt') as inf:
    for line in inf:
        print(line)

