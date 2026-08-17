class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        beg, end = 0, len(numbers) - 1

        while beg < end:
            total = numbers[beg] + numbers[end]
            if total == target:
                return [beg + 1, end + 1]
            elif total > target:
                end -= 1
            else:
                beg += 1


        