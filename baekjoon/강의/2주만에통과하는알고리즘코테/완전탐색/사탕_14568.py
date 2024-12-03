candy = int(input())

answer = 0
for A in range(0, candy + 1):
    for B in range(0, candy + 1):
        for C in range(0, candy + 1):
            if A + B + C == candy:
                if A >= B + 2:
                    if A != 0 and B != 0 and C != 0:
                        if C % 2 == 0:
                            answer += 1

print(answer)
