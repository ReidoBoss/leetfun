# Given an integer array nums and an integer k,
# return the k most frequent elements.
# You may return the answer in any order.

from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        # early return
        if len(nums) == k:
            return nums

        visitedNumbers = defaultdict(int)

        for num in nums:
            visitedNumbers[num] += 1

        sortedFrequents = sorted(
            visitedNumbers.items(), key=lambda num: num[1], reverse=True
        )

        def mapper(dict_item: tuple[int, int]) -> int:
            return dict_item[0]

        result = list(map(mapper, sortedFrequents))

        return result[:k]


print(Solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
