class Solution(object):
        
    def sortColors(self, nums):
        
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            
            if nums[mid] == 0:
                nums_mid = nums[mid]
                nums_low = nums[low]
                
                nums[mid] = nums_low
                nums[low] = nums_mid
                
                low += 1
                mid += 1
                
            elif nums[mid] == 1:
                mid += 1
                
            elif nums[mid] == 2:
                nums_mid = nums[mid]
                nums_high = nums[high]
                
                nums[mid] = nums_high
                nums[high] = nums_mid
                
                high -= 1
                
        return nums
                
                
s = Solution()
print(s.sortColors([2,0,1]))
                
            