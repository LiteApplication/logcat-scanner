import sys

def removeTimeStamp(log):
    #f = sys.stdin.read().split('\n')
    #f.remove('')
    f = log.split('\n')
    f.remove('')

    out = ""

    for i in f:
        x = i.split()
        x.pop(0)
        x.pop(0)
        x.pop(0)
        x.pop(0)

        y = ""
        for j in x:
            y += j + ' '
        out += y + '\n'
    return out

def compareLog(log1,log2):
    repeats = []
    for line in log1:
        if line in log2 and line not in repeats:
            repeats.append(line)
            print(line)
    return repeats


