class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        if s == "":
            return 0
        
        if len(set(s)) == len(s):
            return len(s)
        
        subtring_counter = dict()
        
        for i in range(len(s)):
            subtring_start = s[i]
            current_substring = subtring_start
            
            for j in range(i+1, len(s)):
                subtring_finish = s[j]
                
                if subtring_finish in current_substring:
                    subtring_counter[current_substring] = len(current_substring)
                    break
                
                current_substring += subtring_finish
            
            subtring_counter[current_substring] = len(current_substring)   
        
        print(subtring_counter)
                
        return len(max(subtring_counter, key=subtring_counter.get))
    
    
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
                
                