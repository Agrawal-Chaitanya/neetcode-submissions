class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff_seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diff_seen:
                return [diff_seen[diff], i]
            diff_seen[n]=i
        