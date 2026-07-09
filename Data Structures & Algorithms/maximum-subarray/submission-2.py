class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum_checker = 0

        for i in nums:
            sum_checker += i
            max_sum = max(max_sum, sum_checker)

            if sum_checker < 0:
                sum_checker = 0


        return max_sum