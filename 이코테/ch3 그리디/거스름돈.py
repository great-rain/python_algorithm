money = int(input())

count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += money // coin
    money %= coin

print(count)