# A 가 정답으로 생각할 수 있는 모든 수를 넣어보기

# 그리고 B가 도전한 내용이 맞는지 확인하기

n = int(input())
numbers = [list(map(str,input().split())) for _ in range(n)]

answer = 0
# (1) 세 자리 숫자 만들기
for a in range(1, 10):  # 100의 자리수
    for b in range(1, 10):  # 10의 자리수
        for c in range(1, 10):  # 1의 자리수
            counter = 0

            # (2) 다른 세 자리수
            if (a == b or b == c or c == a):
                continue

            # continue, 그 숫자를 넘김
            # break, 반복문을 넘김

            # (3) 배열에 넣은 조건을 넣어주기
            for array in numbers:
                check = list(array[0])  # ['1','2','3']
                strike = int(array[1])
                ball = int(array[2])

                strike_count = 0
                ball_count = 0

                # 스트라이크 계산기
                if (a == int(check[0])):
                    strike_count += 1
                if (b == int(check[1])):
                    strike_count += 1
                if (c == int(check[2])):
                    strike_count += 1

                # 볼 계산기
                if (a == int(check[1]) or a == int(check[2])):
                    ball_count += 1
                if (b == int(check[0]) or b == int(check[2])):
                    ball_count += 1
                if (c == int(check[0]) or c == int(check[1])):
                    ball_count += 1

                # (4) 매칭 여부 확인하기
                if (strike != strike_count):
                    break
                if (ball != ball_count):
                    break

                counter += 1

            if counter == n:
                answer += 1

print(answer)
