# String

+ [Valid anagram](#valid-anagram)
+ [Reverse string](#reverse-string)
+ [Reverse vowels of a string](#reverse-vowerls-of-a-string)

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        if not s or len(s) <= 1:
            return s
        pointer_1 = 0
        pointer_2 = len(s)-1
        while pointer_1 < pointer_2:
            s[pointer_1], s[pointer_2] = s[pointer_2], s[pointer_1]
            pointer_1 += 1
            pointer_2 -= 1
        return s
``` 

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
class Solution:  
    def getVowel(self, s):
        res = []
        for i in s:
            if i in "aeiouAEIOU":
                res.append(i)
        return res
    
    def reverseVowels(self, s: str) -> str:
        reverse = self.getVowel(s)
        word = ""
        for i in s:
            if i in "aeiouAEIOU":
                word += reverse.pop()
            else:
                word += i
        return word 
```