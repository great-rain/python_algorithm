H, M = map(int, input().split())
cook_time = int(input())

total_cook_time = H * 60 + M + cook_time

cal_min = total_cook_time - 1440 if total_cook_time >=1440 else 1440 + total_cook_time if total_cook_time < 0 else total_cook_time
h = cal_min // 60
m = cal_min % 60
print(h, m)