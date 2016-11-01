import time

class Solution(object):
    def threeSum(self, nums):
        ret = set([])
        l = len(nums)
        for i in range(l):
            st = set([])
            for j in range(i+1,l):
                tmp = 0 - nums[i] - nums[j]
                if nums[j] in st:
                    sl = tuple(sorted([nums[i],nums[j],tmp]))
                    ret.add(sl)
                else:
                    st.add(tmp)
        return [list(tup) for tup in ret]

    def threeSum2(self, nums):
        nums = sorted(nums)
        lens = len(nums)
        ret = []
        for i in range(lens-2):
            if i != 0 and nums[i] == nums[i-1]: continue
            j,k = i+1,lens-1
            print i,j,k
            while j < k:
                anchor = nums[i]+nums[j]+nums[k]
                if anchor < 0:
                    j += 1
                elif anchor > 0:
                    k -= 1
                else:
                    ret.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: j += 1
                    while j < k and nums[k] == nums[k + 1]: k -= 1
        return ret




if __name__ == '__main__':
    # result = Solution().threeSum2([-1, 0, 1, 2, -1, -4])
    result = Solution().threeSum2([0,-4,-1,-4,-2,-3,2])
    print result
