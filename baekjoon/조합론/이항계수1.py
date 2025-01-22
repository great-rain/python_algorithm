N, K = map(int, input().split())

def binomial(n, k):
    if k == 0:
        return 1
    return binomial(n-1, k-1)*n

print(binomial(N, K)//binomial(K, K))