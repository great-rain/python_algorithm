# def remove(s, index):
#     return s[:index] + s[index+1:]
#
# def recursion(number, k, max_number):
#     if k == 0:
#         return max_number
#
#     max_number = number[1:]
#     for i in range(1, len(number)):
#         max_number = str(max(int(remove(number, i)), int(max_number)))
#
#     return recursion(max_number, k - 1, max_number)
# def solution(number, k):
#     max_number = 0
#     return recursion(number, k, max_number)
def solution(number, k):
    answer = []  # Stack

    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

number = '1231234'

print(solution(number, 3))
