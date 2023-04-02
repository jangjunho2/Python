def sliding_window_sum(nums, k):
    if k > len(nums):
        return []
    window_sum = sum(nums[:k])
    result = [window_sum]
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]  # 앞에꺼 뺴고 뒤에꺼 넣음
        result.append(window_sum)
    return result


a = list(range(1, 10))
print(a)
window = sliding_window_sum(a, 3)

print(window)
