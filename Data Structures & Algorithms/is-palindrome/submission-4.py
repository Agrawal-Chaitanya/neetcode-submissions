class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        alphanumeric_ab = ''.join(char for char in s if char.isalnum())
        alphanumeric_ab = alphanumeric_ab.lower()
        right = len(alphanumeric_ab)-1

        while left <= right:
            if alphanumeric_ab[left] != alphanumeric_ab[right]:
                return False
            else:
                left +=1
                right -=1
        return True

        