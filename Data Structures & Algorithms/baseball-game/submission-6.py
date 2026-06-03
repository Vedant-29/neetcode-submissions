class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []


        for each_item in operations:
            if each_item == "+":
                arr.append(arr[-1] + arr[-2])
            elif each_item == "D":
                arr.append(2 * arr[-1])
            elif each_item == "C":
                arr.pop()
            else:
                arr.append(int(each_item))

        return sum(arr)