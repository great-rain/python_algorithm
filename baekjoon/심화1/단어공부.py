import collections
W = [i.upper() for i in input().strip()]

d = collections.defaultdict(int)
for i in W:
    d[i] += 1

value_to_keys = collections.defaultdict(list)
for k, v in d.items():
    value_to_keys[v].append(k)

max_value = max(value_to_keys.keys())
max_key = value_to_keys[max_value]
print(max_key[0] if len(max_key) == 1 else "?")
