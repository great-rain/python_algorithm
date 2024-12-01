num, base = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 0~9 + a~z
result = []

while num > 0:
    remainder = num % base
    result.append(digits[remainder])
    num //= base

print(''.join(reversed(result)))