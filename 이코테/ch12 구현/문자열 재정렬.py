"""
K1KA5CB7

# ABCKK13

AJKDLSI412K4JSJ9D

# ADDIJJJKKLSS20
"""

# 구현
# 초기값 설정
data = input()

alphabet = []
number = []

# 영어, 숫자 분리
for i in data:
    if i.isnumeric():
        number.append(int(i))
    else:
        alphabet.append(i)

# 영어를 오름차순정렬 -> sort() nlogn. dict 이용 하는 방법 10,000
alphabet.sort()

# 숫자 더한 값 추가
print(''.join(alphabet) + str(sum(number)))
