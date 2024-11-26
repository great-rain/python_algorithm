s = input().split(' ')
count = 0
for i in s:
    if i != '':
        count += 1

print(count)

"""
import sys
s = sys.stdin.read().strip()
print(s.count(' ') + 1 if s else 0)
"""