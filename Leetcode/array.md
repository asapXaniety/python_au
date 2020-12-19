# Array

+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape The Matrix](#reshape-the-matrix)
+ [Flipping an Image](#flipping-an-image)
+ [Move Zeroes](#move-zeroes)
+ [Image Smoother](#image-smoother)
+ [Transpose Matrix](#transpose-matrix)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

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

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        Height = len(M)
        Width = len(M[0])
        res = [[0] * Width for _ in range(Height)]
        for i in range(Height):
            for j in range(Width):
                k = 0
                s = 0
                for i_k in range(i-1, i+2):
                    for j_k in range(j-1, j+2):
                        if 0 <= i_k < Height and 0 <= j_k < Width:
                            s = s + M[i_k][j_k]
                            k = k + 1
                res[i][j] = floor(s/k)
        return res
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(A[0])):
            arr = []
            for j in range(len(A)):
                arr.append(A[j][i])
            res.append(arr)
        return res
```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
class Solution:
    
    def get_first_nonnegative(self, A: List[int]):
        for i, val in enumerate(A):
                if val >= 0:
                    return i
        return -1
                              
    def sortedSquares(self, A: List[int]) -> List[int]:
        ind = self.get_first_nonnegative(A)
        if ind == -1:
            return [x ** 2 for x in A[::-1]]
        elif ind == 0:
            return [x ** 2 for x in A]
        else:
            left, right = ind - 1, ind
            length = len(A)
            result = []
            while right < length and left >= 0:
                if A[left] ** 2 < A[right] ** 2:
                    result.append(A[left] ** 2)          
                    left -= 1
                else:
                    result.append(A[right] ** 2)
                    right += 1
            while left >= 0:
                result.append(A[left] ** 2)
                left -= 1
            while right < length:
                result.append(A[right] ** 2)
                right += 1
            return result
```