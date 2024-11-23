x = "+" if int(input()) > 0 else "-"
y = "+" if int(input()) > 0 else "-"

qua = [["+", "+"], ["-", "+"], ["-", "-"], ["+", "-"]]
print(int(qua.index([x,y]))+1)

"""
A,B = map(int,input().split())
print("==" if A == B else "><"[A<B])
"""