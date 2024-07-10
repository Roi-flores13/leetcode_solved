def removeDuplicates(nums):
    k = 0
    while (k+1) < len(nums):
        if nums[k] == nums[k+1]:
            nums.pop(nums[k+1])
            
        else:
            k += 1
            
    print(nums)
    return len(nums)

nums = [-1,0,0,0,0,3,3]
print(removeDuplicates(nums))