N = int(input())
nums = [int(i) for i in input().split()]
count = 0

def is_prime_optimized(num):
    """
    작은 범위에서의 소수 찾기.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    # 6k ± 1 패턴
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


for i in nums:
    if is_prime_optimized(i):
        count += 1

print(count)