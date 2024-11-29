def timsort(data):
    MIN_RUN = 8

    def calc_min_run(n):
        r = 0           # 나머지 비트 플래그 (추가 조정 값)
        while n >= MIN_RUN:
            r |= n & 1  # n의 마지막 비트를 r에 OR 연산으로 저장
            n >>= 1     # n을 1비트 오른쪽으로 시프트 (n을 2로 나눔)
        return n + r

    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(arr, start, mid, end):
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]

        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    n = len(data)
    min_run = calc_min_run(n)

    # Step 1: Divide the array into runs and sort them using insertion sort.
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(data, start, end)

    # Step 2: Iteratively merge runs following Timsort's merging criteria.
    size = min_run
    while size < n:
        for start in range(0, n, 2 * size):
            mid = min(start + size - 1, n - 1)
            end = min(start + 2 * size - 1, n - 1)

            if mid < end:
                merge(data, start, mid, end)

        size *= 2

    return data

# Test the Timsort implementation
if __name__ == "__main__":
    data = [5, 21, 7, 23, 19, 10, 3, 2, 8, 6, 11, 4, 15, 20]
    print("Original array:", data)
    sorted_data = timsort(data)
    print("Sorted array:", sorted_data)
