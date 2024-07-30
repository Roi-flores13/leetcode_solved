class Solution:
    def thirdMaximum(self, nums):
        individual = set(nums)
        if len(individual) < 3:
            return max(individual)
        
        return sorted(individual)[-3]

        