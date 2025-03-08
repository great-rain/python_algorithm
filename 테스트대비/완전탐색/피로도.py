from itertools import permutations


def solution(k, dungeons):
    dungeonlist = list(permutations(dungeons))
    max_count = 0

    for dun in dungeonlist:
        pirodo = k
        count = 0
        for d in dun:
            if pirodo >= d[0]:
                pirodo -= d[1]
                count += 1
        max_count = max(max_count, count)

    return max_count

k, dungeons = 80, [[80,20],[50,40],[30,10]]


print(solution(k, dungeons))