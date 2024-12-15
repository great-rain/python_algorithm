N = int(input())

series = 666
count = 1
while count <= N:
    if str(series) in '666':
        count += 1
    series += 8

print(series)