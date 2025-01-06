# 2차배열 생성하기
def create_2d_array(x, y):
    return [[0 for _ in range(y)] for _ in range(x)]

# 예시: x=3, y=4
x = 3
y = 4
array_2d = create_2d_array(x, y)

# 결과 출력
for row in array_2d:
    print(row)
