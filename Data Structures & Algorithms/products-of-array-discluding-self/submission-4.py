class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1

        prod_left = [1]
        prod_right = [1]*len(nums)

        for i in range(1, len(nums)):
            prod_left.append(nums[i-1]*prod_left[i-1])

        for j in range(len(nums)-2, -1, -1):
            prod_right[j] =nums[j+1]*prod_right[j+1]

        return [prod_left[i]*prod_right[i] for i in range(len(nums))]