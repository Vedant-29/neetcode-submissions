class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter = 0
        daily_counter = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                daily_counter += 1
            else:
                if daily_counter > max_counter:
                    max_counter = daily_counter
                daily_counter = 0
            
        if daily_counter > max_counter:
            max_counter = daily_counter
            
        return max_counter