"""
					1						1
				1		1					2
			1		2		1				4
		1		3		3		1			8
	1		4		6		4		1		16

"""
N = int(input())
def green_top(diff, stage):
    if stage == 1:
        return 2
    return green_top(diff - 1, stage-1) + 2**diff

print(green_top(N-1, N))