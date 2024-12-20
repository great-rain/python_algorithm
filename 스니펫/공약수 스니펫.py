

# 두 수 에 대한 스니펫
def gcd(a, b):
    """
    유클리드 호제법을 사용하여 최대공약수를 구합니다.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    두 수의 최소공배수를 계산합니다.
    """
    return a * b // gcd(a, b)

def get_divisors(n):
    """
    특정 수의 모든 약수를 구합니다.
    """
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

