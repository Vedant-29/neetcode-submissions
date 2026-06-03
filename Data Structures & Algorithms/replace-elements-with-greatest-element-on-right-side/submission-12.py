class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_element = -1

        for i in range(len(arr) - 1, -1, -1):
            var_arr = arr[i]
            arr[i] = greatest_element
            greatest_element = max(var_arr, arr[i])



        return arr
        

            