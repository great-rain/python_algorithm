while True:
    n = int(input())
    if n == -1: break

    divisor = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            divisor.append(n // i)
    divisor = sorted(divisor)
    if sum(divisor) == n:
        result = f'{n} = '
        for i in range(len(divisor)-1):
            result += f'{divisor[i]} + '
        result += f'{divisor[-1]}'
        print(result)
    else:
        print(f"{n} is NOT perfect.")