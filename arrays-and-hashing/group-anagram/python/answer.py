# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            result[key].append(string)

        return list(result.values())


print(Solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
