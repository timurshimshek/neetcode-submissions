class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x ={}
        r = 0
        for i in nums:
            if i in x:
                if target == 2 * i:
                    return [x[i], r]
            else:
                x[i] = r
            r +=1
        for i in x:
            if target -i in x and target- i != i:
                return [x[i], x[target-i]]