N, M = map(int, input().split())
bucket = [0] * N


def input_ball(bucket: list, i: int, j: int, k: str):
    for idx in range(i - 1, j):
        bucket[idx] = k
    return bucket


for _ in range(M):
    i, j, k = map(int, input().split())
    bucket = input_ball(bucket, i, j, k)

print(" ".join(map(str, bucket)))