a = int(input('введите первое число'))
b = int(input('введите второе число'))
c = int(input('введите третье число'))

m = a
if (m < b):
    m = b
elif (m < c):
    m = c

l = a
if (l > b):
    l = b
elif (l > c):
    l = c

if (l < a < m) or (l < a <= m):
    ml = a
elif (l <= b < m) or (l < b <= m):
    ml = b
elif (l <= c < m) or (l < c <= m):
    ml = c

print (m,'\n',l,'\n',ml)