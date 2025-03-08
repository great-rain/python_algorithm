from itertools import permutations


def checkPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    answer = []
    numbers = list(numbers)
    temp = []

    for i in range(1, len(numbers) + 1):
        temp += list(permutations(numbers, i)) # 반복 가능한(iterable) 객체에서 원소를 중복 없이 나열할 수 있는 모든 순열을 생성하는 데 사용됩니다.
    num = [int(''.join(t)) for t in temp]

    for i in num:
        if checkPrime(i):
            answer.append(i)

    return len(set(answer))