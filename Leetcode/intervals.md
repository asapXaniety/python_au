# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)

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
