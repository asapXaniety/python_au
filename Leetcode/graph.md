# Graph

+ [Course Schedule II](#course-schedule-ii)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
def findOrder(self, nc, prerequisites):
        gr = [[] for _ in range(nc)]
        indegree = [0 for _ in range(nc)]
        for course, prev in prerequisites:
            gr[prev].append(course)
            indegree[course] += 1
        queue = []
        for course in range(nc):
            if indegree[course] == 0:
                queue.append(course)
        res = []
        while queue:
            course = queue.pop(0)
            res.append(course)
            for nei in gr[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(res) == nc:
            return res
        else:
            return []
```