N = int(input())

trees = []
diff = []
for _ in range(N):
    trees.append(int(input()))
trees.sort()
for i in range(N - 1):
    diff.append(trees[i + 1] - trees[i])


def gcd_list(numbers):
    """
    리스트에서 최대공약수 구하기
    """

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    result = numbers[0]
    for number in numbers[1:]:
        result = gcd(result, number)
        if result == 1:
            return 1
    return result


gcd = gcd_list(diff)
result = 0
for i in diff:
    result += i // gcd - 1 # 들어가는 갯수 이므로 나눈 뒤 1을 빼준다

print(result)
