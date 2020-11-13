# Math

+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Fibonacci Number](#fibonacci-number)
+ [Base 7](#base-7)
+ [Sqrt(x)](#sqrtx)

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

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output=[]
        for i in range(1,n+1):
            if (i % 3 ==0 and i % 5 == 0):
                output.append("FizzBuzz")
            elif i %5==0:
                output.append("Buzz")
            elif i %3==0:
                output.append("Fizz")
            else:
                output.append(str(i))           
        return output
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
class Solution:
    def fib(self, N: int) -> int:
        x1 = 0
        x2 = 1
        if N < 0:
            return x1
        if N == 1:
            return x2
        if N > 30:
            return 0
        for _ in range(N):
            x1 , x2 = x2, x1+x2
        return x1
```

## Base 7

https://leetcode.com/problems/base-7/

```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        s = []
        n = num
        num = abs(num)
        while num>0:
            s.append(str(num%7))
            num = num // 7
        if n > 0:
            return ''.join(reversed(s))
        else:
            sign = '-'
            s.append(sign)
            return ''.join(reversed(s))
```

## sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        lower = 0
        if x > 5: 
            upper = x // 2
        else:
            upper = x
        middle = (lower + upper) // 2
        while True:
            if x == middle * middle:
                return middle
            elif x < middle * middle:
                upper = middle
            else:
                lower = middle
            if middle == (lower + upper) // 2:
                return middle
            middle = (lower + upper) // 2
```