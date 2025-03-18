# 순서가 뒤죽박죽

# 정렬 -> nlogn 

# 가운데 숫자부터 비교 

# 1 2 3 4 5 10 12 14 100 
# 4 3 2 1 0 5 7 9 95 -> 122
# 9 8 7 6 5 0 2 4 90 -> 
n = int(input())
data = list(map(int, input().split()))
data.sort()


print(data[(n-1)//2])