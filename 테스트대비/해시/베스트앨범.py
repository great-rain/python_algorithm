genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
# def solution(genres, plays):
#     answer = []
#     total_genre_d = {}
#
#     temp = [[genres[i], plays[i], i] for i in range(len(genres))]  # [장르, 재생횟수, 고유 번호] 리스트
#     temp = sorted(temp, key=lambda x: (x[0], -x[1], x[2]))  # 많이 재생될수록, 같다면 고유번호가 낮을수록
#
#     for g in temp:  # {장르 : 총 재생횟수} 딕셔너리 생성
#         if g[0] not in total_genre_d:
#             total_genre_d[g[0]] = g[1]
#         else:
#             total_genre_d[g[0]] += g[1]
#
#     total_genre_d = sorted(total_genre_d.items(), key=lambda x: -x[1])  # 재생횟수가 많은 순서로 장르 정렬
#
#     for i in total_genre_d:  # 같은 장르 내에서는 최대 2곡까지 조건대로 수록
#         count = 0
#         for j in temp:
#             if i[0] == j[0]:
#                 count += 1
#                 if count > 2:
#                     break
#                 else:
#                     answer.append(j[2])
#
#     return answer

def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

print(solution(genres, plays))
