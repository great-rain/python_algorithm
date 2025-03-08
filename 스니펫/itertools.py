from itertools import permutations, combinations, product, combinations_with_replacement


# Python의 itertools 모듈은 반복 가능한 데이터를 효율적으로 처리하기 위한 많은 도구를 제공합니다. \
# 코딩 테스트에서 유용하게 사용될 수 있는 몇 가지 기능에 대해 설명하고 예시 코드를 보여드리겠습니다.
# 1. permutations
# itertools.permutations은 입력된 반복 가능한 데이터에서 모든 가능한 순서의 순열을 생성합니다.
# 예를 들어, 리스트 [1, 2, 3]의 모든 순열을 생성할 수 있습니다.

data = [1, 2, 3]
result = list(permutations(data))
print(result) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 2. combinations
# itertools.combinations은 주어진 반복 가능한 데이터에서 지정된 길이의 모든 조합을 생성합니다.
# 예를 들어, [1, 2, 3, 4]에서 2개를 선택하는 모든 조합을 찾을 수 있습니다.


data = [1, 2, 3, 4]
result = list(combinations(data, 2))
print(result) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# 3. product
# itertools.product는 여러 반복 가능한 데이터의 데카르트 곱을 생성합니다.
# 예를 들어, 두 개의 리스트 [1, 2]와 ['a', 'b']의 모든 조합을 생성할 수 있습니다.

numbers = [1, 2]
letters = ['a', 'b']
result = list(product(numbers, letters))
print(result) # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# 4. combinations_with_replacement
# 이 함수는 주어진 반복 가능한 데이터에서 원소를 중복 허용하여 지정된 길이의 조합을 생성합니다.

data = [1, 2, 3]
result = list(combinations_with_replacement(data, 2))
print(result) # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]