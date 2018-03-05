import sys
r=''
for i in open(sys.argv[1]).read():
    if i=='>':
        r+='chris '
    elif i=='<':
        r+='lee '
    elif i=='+':
        r+='lol '
    elif i=='-':
        r+='rip '
    elif i=='[':
        r+='chris? '
    elif i==']':
        r+='lee? '
    elif i=='.':
        r+='ok '
    elif i==',':
        r+='pls '
print r