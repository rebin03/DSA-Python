class Solution:
    def twoSum(self, numbers, target):

        start = 0
        end = len(numbers)-1
        curr_sum = numbers[start] + numbers[end]

        while curr_sum != target:

            curr_sum = numbers[start] + numbers[end]

            if curr_sum > target:
                end -= 1
            elif curr_sum < target:
                start += 1

        return [start+1, end+1]