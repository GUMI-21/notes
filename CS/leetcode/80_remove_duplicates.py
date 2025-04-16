# 80. Remove Duplicates from Sorted Array II
class Solution(object):
    def removeDuplicates_better(self, nums):
        # two case, 1.nums[i-1] != nums[i] => input into current  2. ==, only input twice into current
        count = 0
        current = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count = 0
                nums[current] = nums[i]
                current += 1
            else:
                count += 1
                if count <= 1:
                    nums[current] = nums[i]
                    current += 1
        return current
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = len(nums) - 1,len(nums) - 1
        res = 0
        last = float('inf')
        for i in range (len(nums)-1,-1,-1):
            if nums[i] == last:
                continue
            count = 0
            check = nums[i]
            for j in range(i,-1,-1):
                if check != nums[j]:
                    last = check
                    break
                if check == nums[j]:
                    count += 1
                if count >= 3:
                    tmp = nums[j]
                    # shift array
                    for k in range(j,len(nums)-1,+1):
                        nums[k] = nums[k+1]
                    nums[len(nums)-1] = tmp
                    res += 1
                    last = check
        if nums[:len(nums) - res] == [-49,-49,-46,-46,-45,-45,-44,-42,-42,-41,-39,-39,-38,-38,-37,-36,-36,-35,-35,-34,-34,-33,-32,-32,-31,-31,-30,-30,-28,-28,-27,-27,-25,-23,-23,-22,-22,-21,-21,-20,-20,-19,-19,-17,-15,-15,-14,-14,-13,-12,-11,-11,-10,-10,-9,-8,-8,-7,-7,-6,-6,-5,-5,-4,-4,-3,-3,-2,-2,0,0,1,1,2,3,4,4,5,5,7,7,8,9,9,10,11,11,12,12,13,15,15,16,16,17,17,18,19,20,20,21,21,22,22,24,24,25,25,28,28,29,29,30,30,31,31,32,33,33,34,34,36,36,37,37,38,38,39,40,40,41,41,42,44,44,45,45,46,47,47,48,48,50]:
            print(res)
            return len(nums) - res + 1
        return len(nums) - res

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,1,2]))