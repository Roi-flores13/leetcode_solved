s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    s_altered = "".join(letter for letter in s.lower() if letter.isalnum())
    
    if s_altered != s_altered[::-1]:
        return False
    
    return True

print(isPalindrome(s))