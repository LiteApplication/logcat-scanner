import sys

def removeTimeStamp():

    f = sys.stdin.read().split('\n')
    f.remove('')
    
    out = ""

    for i in f:
        x = i.split()
        x.pop(0)
        x.pop(1)
    
        y = ""
        for j in x:
            y += j + ' '
        out += y + '\n'
    return out

