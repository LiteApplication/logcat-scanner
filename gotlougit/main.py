import sys

f = sys.stdin.read().split('\n')
f.remove('')

for i in f:
    x = i.split()

    x.pop(0)
    x.pop(1)
    
    for j in x:
        print(j,end=" ")
    print()
