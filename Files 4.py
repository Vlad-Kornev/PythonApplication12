with open ('file.txt') as inf:
    t = inf.readline()
    t1 = t[1]
    print(t1.isdigit())