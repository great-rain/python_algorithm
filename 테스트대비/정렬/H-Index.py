def solution(citations):
    answer = 0
    citations.sort(reverse = True) # 내림차순으로 정렬
    for num, citation in enumerate(citations):
        # 피 인용수가 논문의 수랑 같아지는 지점(num은 0부터 시작하니까 +1)
        if citation >= num+1:
            h_index = num+1
            answer = h_index

    return answer
# citations = [0,1,3,5,6]
citations = [2,4,6,8,10]
# citations = [1,3,5, 13,14,15]
# citations = [1,2,3,4,5,6]
print(solution(citations))