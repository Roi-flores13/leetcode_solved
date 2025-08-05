class Solution():
    def restoreIPAdress(self, s):
        
        res = []
        
        def is_valid(segment):
            if not segment.isdigit():
                return False
            
            if not int(segment) in range(0, 256):
                return False
            
            if len(segment) > 1 and segment[0] == "0":
                return False
            
            return True
        
        def backtrack(pos, path):
            
            if len(path) == 4:
                if pos == len(s):
                    valid_ip = ".".join(path)
                    res.append(valid_ip)
                else:
                    return 
                
            for i in range(1, 4):
                if pos + i <= len(s):
                    segment = s[pos: pos+i]
                    
                    if is_valid(segment):
                        path.append(segment)
                        backtrack(pos + i, path)
                        path.pop()
                
        backtrack(0, [])
        return res        
s = Solution()

print(s.restoreIPAdress("25525511135"))
                
                



