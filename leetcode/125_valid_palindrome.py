"""125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""
from html.parser import charref

# double finger pointer
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j = 0,len(s)-1
        while i<j:
            check1 = 0
            check2 = 0
            if s[i].isalnum():
                if s[i].isalpha():
                    check1 = s[i].lower()
                else:
                    check1 = s[i]
            else:
                i += 1
                continue

            if s[j].isalnum():
                if s[j].isalpha():
                    check2 = s[j].lower()
                else:
                    check2 = s[j]
            else:
                j -= 1
                continue
            if check1 != check2:
                return False
            i += 1
            j -= 1
        return True
