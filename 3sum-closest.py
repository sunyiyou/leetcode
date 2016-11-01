class Solution(object):
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        lens = len(nums)
        mindist = float("inf")
        for i in range(lens-1):
            if i != 0 and nums[i] == nums[i-1]: continue
            j,k = i+1,lens-1
            while j < k:
                print i,j,k
                dist = nums[i] + nums[j] + nums[k] - target
                if abs(dist) < abs(mindist):   mindist = dist
                if dist < 0: j += 1
                elif dist > 0: k -= 1
                else: return target
        return mindist + target


if __name__ == '__main__':
    s = Solution()
    # nums = [1,2,4,8,16,32,64,128]
    nums = [0,1,1,1]
    target = 82
    print s.threeSumClosest(nums,target)
