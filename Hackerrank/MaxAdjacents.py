def solution(nums):
    
    if len(nums) < 2:
        return None

    max_product = nums[0] * nums[1]

    for i in range(1, len(nums) - 1):
        current_product = nums[i] * nums[i + 1]
        max_product = max(max_product, current_product)

    return max_product
