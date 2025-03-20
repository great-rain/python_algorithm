import math

def solution(progresses, speeds):
    work_day = []
    stack = []
    answer = []
    for pro, sp in zip(progresses, speeds):
        work_day.append(math.ceil((100-pro)/sp))

    for day in work_day:
        if not stack:
            stack.append(day)
        else:
            if stack[0] >= day:
                stack.append(day)
            elif stack[0] < day:
               answer.append(len(stack))
               stack = [day]
    if stack:
        answer.append(len(stack))

    return answer

progresses, speeds = [93, 30, 55], [1, 30, 5]
progresses, speeds = [95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))