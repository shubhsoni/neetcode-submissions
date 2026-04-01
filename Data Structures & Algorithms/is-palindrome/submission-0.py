class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss =  s.replace(' ','')
        ss = ''.join([char.lower() for char in ss if char.isalnum()])
        print(ss)
        return ss == ss[::-1]