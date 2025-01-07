N = int(input())
peoples = sorted(list(map(int, input().split())))
res = 0
l = len(peoples)
for i in peoples:
    res += i * l
    l -= 1
print(res)

"""
1                  res 0 i 1
1 + 2              res 1 i 2
1 + 2 + 3          res 3 i 3
1 + 2 + 3 + 3      

"""