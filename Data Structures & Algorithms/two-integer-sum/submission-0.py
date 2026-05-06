class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ran={}

        for i in range(len(nums)):
            num=nums[i]
            comp=target-num

            if comp in ran:
                return ([ran[comp],i])

            ran[num]=i    