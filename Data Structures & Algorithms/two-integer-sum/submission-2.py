class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trashash = {}

        for i , val in enumerate(nums):
            diff = target - val
            if diff in trashash:
                return [trashash[diff], i]
            trashash[val] = i
