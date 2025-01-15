import sys


def kantoer(s:list)->list:
    if len(s)==1:
        return ['-']

    start = len(s)//3
    end = len(s)//3*2 - 1
    if start == end:
        return ['-', ' ', '-']
    return kantoer(s[0:start]) + [' ']*start + kantoer(s[end+1:])

for line in sys.stdin:
    s = '-'*3**int(line.strip())
    print(''.join(kantoer(s)))