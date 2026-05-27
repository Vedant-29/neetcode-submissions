class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cntr = 0
        max_c = 0

        for n in nums:
            if n == 1:
                cntr += 1
                max_c = max(max_c, cntr)
                print("cntr", cntr)
            else:
                print("max valu", max_c)
                print("cntr", cntr)
                max_c = max(max_c, cntr)
                print("max valu", max_c)
                cntr = 0

        return max_c

