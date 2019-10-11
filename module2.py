a = int(input('введите сторону a: '))
b = int(input('введите сторону b: '))
c = int(input('введите сторону c: '))

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print (s)
