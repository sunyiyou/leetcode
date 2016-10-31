import time

class Solution(object):
    def threeSum(self, nums):
        ret = set([])
        l = len(nums)
        print "%.6f" % time.time()
        for i in range(l):
            st = set([])
            for j in range(i+1,l):
                tmp = 0 - nums[i] - nums[j]
                if nums[j] in st:
                    sl = tuple(sorted([nums[i],nums[j],tmp]))
                    ret.add(sl)
                else:
                    st.add(tmp)
        print "%.6f" % time.time()
        return [list(tup) for tup in ret]



if __name__ == '__main__':
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print "%.6f" % time.time()
    print result
