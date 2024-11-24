from collections import Counter
dice = list(map(int, input().split()))

counter = Counter(dice)
if len(counter) == 1:
    print(10000 + dice[0] * 1000)

elif len(counter) == 2:
    print(counter.most_common()[0][0] * 100 + 1000)

else:
    print(max(dice) * 100)