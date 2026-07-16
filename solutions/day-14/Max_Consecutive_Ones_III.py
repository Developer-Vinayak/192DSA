class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        res = 0
        rem = k
        while r < len(nums):
            if nums[r] == 1:
                r += 1
                res = max(res, r - l)

            elif nums[r] == 0:
                if rem > 0:
                    r += 1
                    rem -= 1
                    res = max(res, r - l)

                elif rem == 0:
                    while nums[l] != 0:
                        l += 1
                    l += 1
                    rem += 1

        return res
