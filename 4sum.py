import time
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        t1 = time.time()
        nums = sorted(nums)
        lens = len(nums)
        ret = []
        for i in range(lens-3):
            if i != 0 and nums[i] == nums[i-1]:continue
            #This part of code has reduce time
            if target < nums[i]*4 or target > nums[-1]*4: continue
            for j in range(i+1,lens-2):
                if j != i+1 and nums[j] == nums[j-1]:continue
                if target-nums[i] < nums[j]*3 or target-nums[i] > nums[-1]*3: continue  #This part of code save 900ms time
                k,l = j+1,lens-1
                while k < l:
                    anchor = nums[i] + nums[j] + nums[k] + nums[l] - target
                    if anchor < 0: k += 1
                    elif anchor > 0: l -= 1
                    else:
                        ret.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]: k += 1
                        # while k < l and nums[l] == nums[l+1]: l -= 1   #This part of code is also unnecessary and waste time
        print "%.6f" % (time.time() - t1)
        return ret

    def fourSum2(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        t1 = time.time()
        results = []
        findNsum(sorted(nums), target, 4, [], results)
        print  "%.6f" % (time.time() - t1)
        return results

if __name__ == '__main__':
    s = Solution()
    nums = range(-100,100)
    target = -1
    s.fourSum(nums,target)
    s.fourSum2(nums,target)