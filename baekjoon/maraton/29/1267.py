"""
영식 -> 30 초 마다 10원. 29 -> 10, 30 ~ 59 -> 20, 60~89 -> 30
민식 -> 60 초 마다 15원. 59 -> 15, 60 ~ 119 -> 30     0 ~ 0.999 -> 0 1~1.9999 -> 0
"""
N = int(input())
receipt = list(map(int, input().split()))


def check_price(receipt: list, person: str) -> list:
    if person == 'Y':
        w = 30
        c = 10
    else:
        w = 60
        c = 15

    price = 0
    for i in receipt:
        price += (i // w + 1) * c

    return [person, price]


Y = check_price(receipt, person='Y')
M = check_price(receipt, person='M')

if Y[1] > M[1]:
    print(*M)
elif Y[1] < M[1]:
    print(*Y)
else:
    print(f"Y M {Y[1]}")
