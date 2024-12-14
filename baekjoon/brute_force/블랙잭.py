N, D = map(int, input().split())
card = [i for i in map(int, input().split())]

smallest_sum = 0
for i in range(len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            sum_num = card[i] + card[j] + card[k]
            if sum_num <= D:
                if D - sum_num <= D - smallest_sum:
                    smallest_sum = sum_num
print(smallest_sum)