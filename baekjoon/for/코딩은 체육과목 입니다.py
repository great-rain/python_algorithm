num = int(input())
r = ["long" for i in range(num//4)] + ["int"]
print(' '.join(r))

# print(int(input())//4*'long ' + 'int')