def solution(name):
    # up = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    # down = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N']
    alphabet = {'A' : 0,'B' : 1 ,'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 12, 'P' : 11, 'Q' : 10, 'R' : 9, 'S' : 8, 'T' : 7, 'U' : 6, 'V' : 5, 'W' : 4, 'X' : 3, 'Y' : 2, 'Z' : 1}
    # 알파벳 변경 횟수( 상하 이동 )
    spell_move = 0

    # 커서 이동 횟수, 이름의 길이 - 1( 좌우 이동 )
    cursor_move = len(name) - 1

    for i, spell in enumerate(name):
        # 알파벳 변경 횟수, 위아래 중 최소 이동 값 ( 상하 이동 )
        spell_move += alphabet[spell]

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 아래 3가지 경우 중 최소 이동 값으로 갱신
        # 1. 이전 커서 이동 값 ( 초기값 - 이름의 길이 - 1 )
        # 2. 연속된 A의 왼쪽 시작
        # 3. 연속된 A의 오른쪽 시작
        cursor_move = min([cursor_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 조이스틱 조작 횟수 = 알파벳 변경 횟수( 상하 이동 ) + 커서 이동 횟수( 좌우 이동 )
    return spell_move + cursor_move

name = "JEROEN"
print(solution(name))