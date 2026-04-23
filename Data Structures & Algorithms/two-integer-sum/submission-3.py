class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x ={}
        r = 0
        for i in nums:
            if target -i in x:
                return [x[target -i], r]
            else:
                x[i] = r
            r += 1