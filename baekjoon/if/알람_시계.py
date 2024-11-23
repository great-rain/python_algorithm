H, M = map(int, input().split())

total_min = H * 60 + M - 45 # 45분 계산 반영

cal_min = total_min - 1440 if total_min >=1440 else 1440 + total_min if total_min < 0 else total_min
h = cal_min // 60
m = cal_min % 60
print(h, m)