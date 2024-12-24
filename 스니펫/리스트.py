# 특정 수가 주어졌을 때 리스트 안의 요소 2개로 그 수를 만들 수 있는 경우의 수를 구하는 방법
def count_pairs_hashmap(lst, target):
    count = 0
    seen = {}
    for num in lst:
        complement = target - num
        if complement in seen:
            count += seen[complement]
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    return count

lst = [1, 2, 3, 4, 5]
target = 6
print(count_pairs_hashmap(lst, target))

# 중복이 없는 경우
def count_pairs_no_duplicates(lst, target):
    count = 0
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            count += 1
        seen.add(num)
    return count

# 중복을 허용하는 경우
# 예시 lst = [1, 2, 3, 4, 5]
# target = 6
# (1,5) (2,4) (3,3)
def count_pairs_with_self_hashmap_no_defaultdict(lst, target):
    seen = {}  # 기본 딕셔너리 사용
    count = 0

    for num in lst:
        complement = target - num

        # 보완 값이 이미 seen에 있으면 카운트 증가
        if complement in seen:
            count += seen[complement]

        # 자기 자신과의 조합 처리
        if num * 2 == target:
            count += 1

        # 현재 숫자를 seen에 추가하거나 갱신
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

    return count
