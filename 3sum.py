class Solution(object):
    def threeSum(self, nums):
        ret = []
        l = len(nums)
        for i in range(l):
            dict = {}
            for j in range(i+1,l):
                tmp = 0 - nums[i] - nums[j]
                if nums[j] in dict:
                    sl = sorted([nums[i],nums[j],tmp])
                    if sl not in ret:
                        ret.append(sl)
                else:
                    dict[tmp]=''
        return ret