class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        visited = set[int]()

        for num in nums:
            if num in visited:
                return True
            visited.add(num)

        return False


print(Solution.containsDuplicate(Solution(), [1, 2, 3, 4, 1]))
print(Solution.containsDuplicate(Solution(), [1, 2, 3, 4]))
