# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        count = 0
        intervals = sorted(intervals, key=lambda x:x[1]) #сортировка по конечному значению
        start_previous = intervals[0][0]
        end_previous = intervals[0][1]
        for i in range(1,len(intervals)): 
            start_next = intervals[i][0]
            end_next = intervals[i][1]
            if  start_next<end_previous:#если начало 2 интервала меньше, чем конец 1, убираем.
                count+=1
            else:
                start_previous = start_next
                end_previous = end_next       
        return count
```


## Merge Intervals

https://leetcode.com/problems/merge-intervals

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals 
        intervals = sorted(intervals, key = lambda x: x[0]) #сортировка по первому значению
        result = [intervals[0]] 
        for interval in intervals[1:]:
            if interval[0] <= result[-1][-1]: #проверка 
                result[-1][1] = max(interval[1], result[-1][1]) # замена конечного числа на максимальное
            else:
                result.append(interval) #добавление интервала
        return result
```


## Insert Interval

https://leetcode.com/problems/insert-interval

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for n, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                result.append(interval)
                
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[n:]
            
            else: 
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                
        result.append(newInterval)
        return result
```



