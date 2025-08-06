class Solution(object):
    def plusOne(self, digits):
        
        if digits[-1] == 9:
            is_nine = True
            idx = -1
            
            while is_nine:
                if digits[idx] == 9 and len(digits) > -idx:
                    idx -= 1
                    
                else:
                    is_nine = False
                    
            if digits[idx] == digits[0] and digits[0] == 9:
                new_list = [0] * -idx
                new_list.insert(0, 1)
                return new_list
            
            kept_list = digits[:idx +1]
            changed_list = [0] * len(digits[idx +1:])
            kept_list[-1] += 1
            
            return kept_list + changed_list
            
        else:
            digits[-1] += 1
            
        return digits
    
    
s = Solution()
print(s.plusOne([8,9,9,9]))

