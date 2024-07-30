class Solution:
    def rotate(self, nums, k):
        nums.insert(0, nums[-k:])

        counter = 0
        while k != counter:
            nums.pop(-1)
            counter += 1  
        return nums
    
    
nums = [1,2,3,4,5,6,7]

k = 3

s = Solution()

print(s.rotate(nums, k))