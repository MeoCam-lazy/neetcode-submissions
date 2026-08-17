class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        nums.sort()
        check = False
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return check