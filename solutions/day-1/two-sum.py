def twoSum(nums, target):
    \"\"\"
    Solution: Hash Map
    Time: O(n)
    Space: O(n)
    \"\"\"
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test cases
print(twoSum([2,7,11,15], 9))  # [0,1]
print(twoSum([3,2,4], 6))      # [1,2]
print(twoSum([3,3], 6))        # [0,1]
