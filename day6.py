
#graph
#nodes(0,1,2,3,4)
graph = {
    0:[1,3],
    1:[0,2],
    2:[1,3],
    3:[0,2]
}

print(f"{graph}")
print(f"{graph[0]}")
print(f"{graph[1]}")
print()

#dfs(depth-first search)
def dfs_recursive(node, graph, visited=None):
    if visited is None:
        visited= set()
    visited.add(node)
    print(f"visited:{node}")

    for nei in graph[node]:
        if nei not in visited:
            dfs_recursive(nei,graph,visited)
    return visited
print("start from node 0:")
visited = dfs_recursive(0,graph)
print(f"{sorted(visited)}")

def iterative(start, graph):
    visited = set()
    stack =[start]

    while stack:
        node =stack.pop()
        if node not in visited:
             visited.add(node)
             print(f"visted:{node}")
        for nei  in reversed(graph[node]):
            if nei not in visited:
                stack.append(nei)
    return visited
visited = iterative(0,graph)
print(f"{sorted(visited)}")

#bfs(hight space):
from collections import deque

def bfs (start,graph):
    visited=set()
    queue=deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(f"visited:{node}")

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
    return visited

visited=bfs(0,graph)
print(f"visited:{sorted(visited)}")


#def find_components(graph):
    #visited=()
    #components=[]
    #for node in graph:
       # if node not in visited:
        #    component=dfs_component(node,graph,visited)
         #   components.append(component)
   # return components

def path(start,end,graph):
    queue = deque([(start,[start])])
    visited = {start}

    while queue:
        node,path=queue.popleft()

        if node == end:
            return path 
        
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei,path + [nei]))
    return None
path = path(0,2,graph)
print(f"{path}")





    












        
        
    


