def count_lines(n):
    co = 0
    with open(n) as inf:
        for line in inf:
            co += 1
    return (co)
a = []
b = []
c = []
cu = 0
with open('file.txt') as inf:
    for line in inf:
        a.append(line.strip().split(';'))
for n in a:
    n.remove(n[0])
    c.append(n)
    for d in n:
        cu += int(d)
    b.append(cu/len(n))
    cu = 0
math = 0
phiz = 0
rus = 0
for n in c:
    math += int(n[0]) / len(c)
    phiz += int(n[1]) / len(c)
    rus += int(n[2]) / len(c)
c.clear()
c.append(math)
c.append(phiz)
c.append(rus)
with open('file1.txt','a') as inf:
    for n in b:
        inf.write(str(n))
    for n in c:
        inf.write(str(n))
print(b,c)