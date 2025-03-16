"""
02984

# 576

567

# 210

"""
n = list(map(int, input()))
print(n)
result = 0
if n[0] == 0:
    result += n[1]
else:
    result += n[0] * n[1]

for i in range(2, len(n)):
    if i == 0:
        result += n[i]
    else:
        result *= n[i]

print(result)