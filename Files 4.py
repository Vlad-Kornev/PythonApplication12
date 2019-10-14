with open('file.txt','r') as inf:
    s = inf.readline()
sym = ''
num = ''
res = ''
resfull = ''
for i in range(0,len(s)-1):
    if s[i].isalpha():
        sym = s[i]
        i += 1
    else:
        if s[i+1].isdigit():
            num = s[i]+s[i+1]
            i += 2
            res = sym * int(num)
        else:
            num = s[i]
            i += 1
            res = sym * int(num)
    resfull += res
#with open('file.txt','w') as ouf:
#    ouf.write(resfull)
print(resfull)