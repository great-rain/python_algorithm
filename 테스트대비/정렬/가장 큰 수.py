def sorting(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return sorting(numbers[:-1])



def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=sorting)
    return numbers

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))