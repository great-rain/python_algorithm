N=int(input())
l = list(map(int,input().split()))

print(min(l), max(l))

"""
import sys
a = [int(s) for s in sys.stdin.read().split()[1:]]
print(min(a), max(a))
"""