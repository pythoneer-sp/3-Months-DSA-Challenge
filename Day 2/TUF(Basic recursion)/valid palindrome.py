# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. 
# LeetCode (125)
# Python3 code solved using recursion

def isPalindrome(s: str):
        return check_palindrome(s,0,len(s)-1)

# Helper function
def check_palindrome(s,l,r):
    if l>=r:
        return True
    if not s[l].isalnum():
        return check_palindrome(s,l+1,r)
    if not s[r].isalnum():
        return check_palindrome(s,l,r-1)
    if s[l].lower() != s[r].lower():
        return False
    return check_palindrome(s,l+1,r-1)