class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique_elements = []
        for i in nums:
            if nums.count(i) == 1:  # Only add elements that appear exactly once
                unique_elements.append(i)
        return sum(unique_elements)
