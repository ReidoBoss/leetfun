# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # early error
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


print(Solution.isAnagram(Solution(), "anagram", "anagram"))
print(Solution.isAnagram(Solution(), "rat", "car"))
