class Solution(object):
    def longestCommonPrefix(self, strs):
    
        prefix = ""
        checker = True
        num_prefix = 1
        
        if len(set(strs)) == 1:
            return strs[0]   
             
        while checker:
            previous_prefix = prefix
            prefix = strs[0][:num_prefix]
            for i in strs:
                
                if i[:num_prefix] != prefix:
                    checker = False
                    break
                
            num_prefix += 1
                
        return previous_prefix
                
                    
                
                
s = Solution()
strs = ["flower","flow","flight"]
print(s.longestCommonPrefix(strs))