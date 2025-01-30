# 정렬 코드들
# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 적은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i 부터 1까지 감소
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은거 만나면 멈추기
            break

print(array)

# 퀵 소트
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른 쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
