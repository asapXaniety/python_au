# Math

+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return x
        rev = 0
        num = x
        x = abs(x)
        while x!=0:
            rev = rev * 10 
            rem = x % 10
            rev = rem + rev
            x = x // 10
        if (rev > (2 ** 31) - 1) or (rev < -2 ** 31 ):
            return 0
        if num > 0:
            return rev
        else:
            return -1 * rev
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        rev = 0
        num = x
        x = abs(x)
        while (x > 0):
            last = x % 10    
            x = x // 10 
            rev = rev * 10 + last
        return num == rev
```




