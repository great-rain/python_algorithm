def solution(clothes):
    closet = {}
    result = 1

    for item, category in clothes:
        if closet.get(category, False):
            closet[category].append(item)
        else:
            closet[category] = [item]

    for name in closet.values():
        result *= (len(name)+1)

    return result - 1
closet = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(closet))