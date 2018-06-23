s='stringtoprintinchrislang'

x=0

for i in s:
    l = ''
    j = ord(i)
    if x < j:
        l = 'l'
        while x < j:
            l += 'ol'
            x += 1
    if x > j:
        l = 'r'
        while x > j:
            l += 'i'
            x -= 1
        l += 'p'
    if l: print(l)
    print('ok')
