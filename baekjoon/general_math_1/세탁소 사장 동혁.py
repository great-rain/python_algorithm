coins = [25, 10, 5, 1]

for _ in range(int(input())):
    price = int(input())
    box = [0, 0, 0, 0]
    for idx, coin in enumerate(coins):
        if price // coin > 0:
            box[idx] = price // coin
            price = price % coin
    print(' '.join(map(str, box)))