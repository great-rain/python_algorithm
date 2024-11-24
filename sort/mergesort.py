def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 배열을 두 부분으로 나눔
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 두 부분을 병합
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # 두 배열을 정렬하면서 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소 추가
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 예제
array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(array)
print(sorted_array)
# 출력: [3, 9, 10, 27, 38, 43, 82]