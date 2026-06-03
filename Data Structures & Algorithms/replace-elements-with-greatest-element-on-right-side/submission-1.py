class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = []
        for i in range(len(arr)):
            if i == len(arr) - 1:
                new_arr.append(-1)
            else:
                new_arr.append(max(arr[i+1:]))
            
        return new_arr
                 
