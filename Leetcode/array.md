# Array

+ [Max Consecutive Ones](#max-consecutive-ones)

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        prev_count = 0
        for num in nums:
            if num == 1:
                count += 1
                if count > prev_count:
                    prev_count = count
                    
            else:
                count = 0     
        return prev_count
```