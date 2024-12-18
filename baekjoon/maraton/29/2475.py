import sys
num_list = [i for i in map(int, sys.stdin.read().split())]
result = 0
for i in num_list:
    result += i**2
sys.stdout.write(str(result%10))