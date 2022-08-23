class Solution(object):
    def twoSum(self, nums, target):
        arr = []
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if x + y == target and i != j:
                    arr.append(i)
                    arr.append(j)
                    print (arr)
                    return arr
        