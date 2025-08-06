class Solution(object):
    def wordPattern(self, pattern, s):        
        s_split = s.split(" ")
        
        if len(set(pattern)) != len(set(s_split)):
            return False
        
        if len(s_split) != len(list(pattern)):
            return False
        
        sequence = dict()
        created_set_pattern = []
        
        for i in pattern:
            if i not in created_set_pattern:
                created_set_pattern.append(i)
                
        """for i in s:
            if i not in created_set_s:
                created_set_s.append(i)"""
        
        for index, value in enumerate(created_set_pattern):
            sequence[value] = s_split[index]
            
        for i, v in enumerate(pattern):
            if sequence[v] != s_split[i]:
                return False
            
        return True
                    
pattern = "deadbeef"
s = "d e a d b e e f"

sol = Solution()
print(sol.wordPattern(pattern, s))