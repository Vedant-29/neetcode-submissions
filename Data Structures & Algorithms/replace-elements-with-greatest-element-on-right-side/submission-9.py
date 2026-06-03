class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_element = -1
        new_arr = arr[:]

        for i in range(len(new_arr) - 1, -1, -1):
            if i == len(new_arr) - 1:
                new_arr[i] = greatest_element
                greatest_element = arr[i]
            else:
                new_arr[i] = greatest_element
                if arr[i] > greatest_element:
                    greatest_element = arr[i]

        return new_arr

            