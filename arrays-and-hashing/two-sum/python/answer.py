from typing import List
from collections import defaultdict


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        visited_indeces = defaultdict(int)
        for index, num in enumerate(nums):
            remaining = target - num

            if remaining in visited_indeces:
                return [visited_indeces[index], index]

            visited_indeces[num] = index

        return []


expectedAnswer1 = [0, 1]
expectedAnswer2 = [1, 2]
expectedAnswer3 = [0, 1]

answer1 = Solution.twoSum([2, 7, 11, 15], 9)
answer2 = Solution.twoSum([3, 2, 4], 6)
answer3 = Solution.twoSum([3, 3], 6)

assert answer1 == expectedAnswer1
assert answer2 == expectedAnswer2
assert answer3 == expectedAnswer3

print("Success!")
