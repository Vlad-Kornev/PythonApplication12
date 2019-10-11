a = int(input())
b = int(input())

s = 0
t = 0

for i in range (a,b+1):
    if i % 3 == 0:
        s += i
        t += 1
print (s / t)