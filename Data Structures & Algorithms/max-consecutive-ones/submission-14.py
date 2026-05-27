class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cntr = 0
        max_c = 0

        for n in nums:
            if n == 1:
                cntr += 1
                max_c = max(max_c, cntr)
            else:
                max_c = max(max_c, cntr)
                cntr = 0

        return max_c

