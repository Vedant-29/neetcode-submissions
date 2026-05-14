from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum_total = 0

    for item in nums:
        sum_total += item

    return sum_total

def get_min(nums: List[int]) -> int:
    min = nums[0]

    for item in nums:
        if item < min:
            min = item

    return min


def get_max(nums: List[int]) -> int:
    max = nums[0]

    for item in nums:
        if item > max:
            max = item

    return max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
