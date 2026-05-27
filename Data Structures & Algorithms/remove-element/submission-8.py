from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dumbArr = []

        for i in range(len(nums)):
            if nums[i] == val:
                dumbArr.append(i)
            else:
                if dumbArr:
                    nums[dumbArr[0]] = nums[i]
                    nums[i] = val
                    dumbArr.pop(0)
                    dumbArr.append(i)

        return len(nums) - len(dumbArr)