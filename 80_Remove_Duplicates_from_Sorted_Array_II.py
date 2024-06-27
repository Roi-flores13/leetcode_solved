def removeDuplicates(nums):
    for i in set(nums):
        while nums.count(i) > 2:
            nums.remove(i)
    return nums