import sys,re
from collections import deque

if len(sys.argv)<2:
    print "Usage: 'chris file'"
    sys.exit(0)
prog = open(sys.argv[1]).read()
arr=deque([0])
i=0
prog=re.sub('\s+',' ',prog).split()

def chris():
    global i
    i+=1
    if i>=len(arr):
        arr.append(0)
        
def lee():
    global i
    i-=1
    if i<0:
        arr.appendleft(0)
        i=0

shift=False
j=0

while 1:
    if j>=len(prog):
        break
    
    #print prog[j], arr[i]
    #if arr[i]>100:break
    
    c=prog[j]
    if shift:
        n=int(c)
        if n>=0:
            for i in range(n):
                chris()
        else:
            for i in range(-n):
                lee()
        shift=False
    if c=='chris':
        chris()
    elif c=='lee':
        lee()
    elif c=='chris?':
        if not arr[i]:
            b=0
            for k in range(j, len(prog)):
                if prog[k]=='chris?':
                    b+=1
                elif prog[k]=='lee?':
                    if b==0:
                        j=k+1
                        break
                    else:
                        b-=1
            else:
                break
            continue
    elif c=='lee?':
        if arr[i]:
            b=0
            for k in range(j-1, -1, -1):
                if prog[k]=='lee?':
                    b+=1
                elif prog[k]=='chris?':
                    if b==0:
                        j=k+1
                        break
                    else:
                        b-=1
            else:
                break
            continue
    elif c=='shift':
        shift=True
    elif c=='troll':
        sys.stdout.write(str(arr[i]))
        sys.stdout.flush()
    elif c=='ok':
        sys.stdout.write(chr(arr[i]))
        sys.stdout.flush()
    elif re.sub('l[ol]+','',c)=='':
        arr[i]+=(len(c)-1)/2
    elif re.sub('ri+p','',c)=='':
        arr[i]-=len(c)-2
        if arr[i]<0:
            arr[i]*=-1
    elif c=='rekt':
        arr[i]=0
    elif c=='pls':
        arr[i]=int(input('?'))
    elif c=='gg':
        break
    j+=1
print