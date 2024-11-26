from typing import List

nums = ["A", "B", "C", "D"]

def productExceptSelf(nums: List[str]) -> List[str]:
    out = []
    p = "P"
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p + nums[i]

    p = "T"
    # 오른쪽 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] + p
        p = p + nums[i]

    return out

print(productExceptSelf(nums))