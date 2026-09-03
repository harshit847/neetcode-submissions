class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 not in nums:
                count = 0
                current = num
                while current in nums:
                    count+=1
                    current+=1
                max_count = max(count,max_count)
        return max_count