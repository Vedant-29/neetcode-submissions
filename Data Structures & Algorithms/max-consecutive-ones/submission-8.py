class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter = 0
        daily_counter = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                daily_counter += 1
            else:
                daily_counter = 0    
            max_counter = max(max_counter, daily_counter)
            
        return max_counter