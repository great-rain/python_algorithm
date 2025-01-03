num = int(input()) * int(input()) * int(input())
num_list = [0 for i in range(10)]

for i in str(num):
    num_list[int(i)] += 1

for j in num_list:
    print(j)