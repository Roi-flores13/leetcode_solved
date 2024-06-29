s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    s_altered = "".join(letter for letter in s.lower() if letter.isalnum())
    left = 0
    right = len(s_altered) - 1
    
    for i in range(len(s_altered)):
        if s_altered[left] !=  s_altered[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(isPalindrome(s))