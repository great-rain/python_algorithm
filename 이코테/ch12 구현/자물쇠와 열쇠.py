def rotate_a_matrix_by_90_degree(a):
    C = len(a)      # 행 길이 계산
    R = len(a[0])   # 열 길이 계산

    result = [[0] * C for _ in range(R)]

    for i in range(C):
        for j in range(R):
            result[j][C-i-1] = a[i][j]
    return result