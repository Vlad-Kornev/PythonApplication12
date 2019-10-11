str = input()
substr = 'G'
substr1 = 'C'

p = str.upper().count(substr)
p1 = str.upper().count(substr1)


print (((p + p1) / len(str)) * 100)
