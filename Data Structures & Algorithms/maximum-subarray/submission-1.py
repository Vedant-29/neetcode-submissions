class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum_checker = 0

        for i in nums:
            if (sum_checker + i) < 0:
                max_sum = max(max_sum, sum_checker + i)

                sum_checker = 0
                continue
            
            sum_checker += i
            max_sum = max(max_sum, sum_checker)

        return max_sum 