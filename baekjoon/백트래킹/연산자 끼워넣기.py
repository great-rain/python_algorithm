N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
ops = ['+', '-', '*', '/']
_max = -1e9
_min = 1e9


def calculate(sequence):
    res = sequence[0]
    for i in range(1, len(sequence) - 1, 2):
        if sequence[i] == '+':
            res += sequence[i + 1]
        elif sequence[i] == '-':
            res -= sequence[i + 1]
        elif sequence[i] == '*':
            res *= sequence[i + 1]
        elif sequence[i] == '/':
            if res // sequence[i+1] < 0:
                res = -(abs(res) // abs(sequence[i+1]))
            else:
                res //= sequence[i + 1]
    return res


def recur(num_idx, sequence, operators):
    global _max
    global _min

    sequence.append(numbers[num_idx])
    num_idx += 1

    if len(sequence) == N * 2 - 1:
        _max = max(_max, calculate(sequence))
        _min = min(_min, calculate(sequence))
        return

    for op in range(len(operators)):
        if operators[op] > 0:
            operators[op] -= 1
            recur(num_idx, sequence + [ops[op]], operators)
            operators[op] += 1


recur(0,[], operators)
print(_max)
print(_min)
