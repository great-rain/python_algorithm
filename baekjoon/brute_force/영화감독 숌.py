N = int(input())

series = 665
count = 0
while count < N:
    series += 1

    if '666' in str(series):
        count += 1

print(series)

"""
1    666
2    1666
3    2666
4    3666
5    4666
6    5666
666
"""