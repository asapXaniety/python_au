# Array

+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape The Matrix](#reshape-the-matrix)
+ [Flipping an Image](#flipping-an-image)

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

## Reshape The Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
            return nums
        if not nums:
            return nums
        new_arr, res, k = [], [], c
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                    new_arr.append(nums[i][j])
                    k -= 1
                    if not k:
                        res.append(new_arr)
                        new_arr = []
                        k = c
        return res
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]: 
        for i in range(len(A)):
            A[i].reverse()
            for j in range(len(A[i])):
                A[i][j] = 1 - A[i][j]
        return A
```
