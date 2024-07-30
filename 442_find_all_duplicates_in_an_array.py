class Solution(object):
    def findDuplicates(self, nums):
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
                
        duplicates = []     
           
        for key, values in counter.items():
            if values == 2:
                duplicates.append(key)
                
        return duplicates

