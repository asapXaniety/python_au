# Graph

+ [Course Schedule II](#course-schedule-ii)
+ [Course Schedule](#course-schedule)
+ [Number of Islands](#number-of-islands)
+ [Is Graph Bipartite](is-graph-bipartite)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)

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

## Course Schedule

https://leetcode.com/problems/course-schedule/

```python
def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    g = [0] * numCourses
    for v, u in prerequisites:
        graph[u].append(v)
        g[v] += 1
    S = [ v for v in range(numCourses) if g[v] == 0]
    while S:
        u = S.pop()
        for v in graph[u]:
            g[v] -= 1
            if g[v] == 0:
                S.append(v)
    return not any(g)
```

## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
def numIslands(self, grid):
    r=len(grid)
    c=len(grid[0])
    cnt=0
    dirn=[(-1,0),(0,-1),(1,0),(0,1)]
    for i in range(r):
        for j in range(c):
            if(grid[i][j]=="1"):
                stack=[]
                stack.append([i,j])
                cnt=cnt+1
                while(len(stack)>0):
                    [p,q]=stack.pop()
                    for k,l in dirn:
                        if(0<=p+k<r and 0<=q+l<c):
                            if(grid[p+k][q+l]=="1"):
                                stack.append([p+k,q+l])
                    grid[p][q]=0
    return cnt
```

## Is Graph Bipartite

https://leetcode.com/problems/is-graph-bipartite/

```python
def isBipartite(self, graph):
    colors = [0]*len(graph) 
        
    def dfs(node, node_color): 
        if colors[node] != 0:
            return colors[node] == node_color           
            
            
        colors[node] = node_color                   
        for neighbor in graph[node]:                
            if not dfs(neighbor, -1*node_color):    
                return False
        return True 
        
    for node in range(len(graph)):
        if colors[node] == 0 and not dfs(node, 1):  
            return False                            
            
    return True
```

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
def findCheapestPrice(self, n, flights, src, dst, K):
	graph = defaultdict(list)
	for u, v, w in flights:
		graph[u].append((v, w))

	# dist, idx, path_len
	q = [(0, src, 1)]
	max_path_len = K + 2
	while q:
		dist, idx, path_len = heappop(q)
		if path_len > max_path_len:
			continue
		if idx == dst:
			return dist
		for v, w in graph[idx]:
			heappush(q, (dist+w, v, path_len+1))
	return -1
```

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
def shortestPathBinaryMatrix(self, grid):
    if grid[0][0] or grid[-1][-1]:
        return -1
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    q = deque([(0, 0, 1)])
        
    while q:
        i, j, steps = q.popleft()
        if (i, j) == (rows-1, cols-1):
            return steps
        for di, dj in directions:
            ii, jj = i+di, j+dj
            if 0 <= ii < rows and 0 <= jj < cols and not grid[ii][jj]:
                grid[ii][jj] = 1  # mark as visited
                q.append((ii, jj, steps + 1))
    return -1
```

## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
def maxDepth(self, root):
    if root == None:
        return 0
    else:
        maxi = 0
        for i in root.children:
            maxi = max(maxi, self.maxDepth(i))
        return 1+maxi
```
