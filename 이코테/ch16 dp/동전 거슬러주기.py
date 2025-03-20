def min_coins(amount, coins):
    coins.sort(reverse=True)  # 큰 금액부터 정렬
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # 최소 동전 개수를 찾았으므로, 각 동전별 개수 계산
    coin_count = {coin: 0 for coin in coins}
    remaining = amount
    for coin in coins:
        if remaining >= coin:
            count = remaining // coin
            while count > 0 and dp[remaining - count * coin] + count != dp[remaining]:
                count -= 1
            coin_count[coin] = count
            remaining -= count * coin

    return coin_count


# 동전 종류 입력
coins = list(map(int, input("사용할 동전 종류를 입력하세요 (공백으로 구분): ").split()))
amount = int(input("거스름돈을 입력하세요: "))
result = min_coins(amount, coins)

print("최소한의 동전 개수:")
for coin, count in result.items():
    print(f"{coin}원: {count}개")
