loc = input()
row = int(loc[1])
col_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
col = col_dict[loc[0]]

step_case = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-2, 1), (-2, -1)]

res = 0
for step in step_case:
    next_row = row + step[0]
    next_col = col + step[1]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        res += 1
print(res)
