from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    distances = {}
    
    heap = []
    
    heappush(heap, (0, 0, source))
    
    visited = set()

    while heap:
        dist, num_edges, current_node = heappop(heap)

        if current_node in visited:
            continue

        distances[current_node] = (dist, num_edges)
        
        visited.add(current_node)

        neighbors = graph.get(current_node, [])
        
        for i in range(len(neighbors)):
            
            neighbor, weight = neighbors[i]
            
            if neighbor not in visited:
                
                heappush(heap, (dist + weight, num_edges + 1, neighbor))

    return distances
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {}
    
    visited = set()
    
    queue = deque([source])
    
    visited.add(source)

    while queue:
        current_node = queue.popleft()

        neighbors = graph.get(current_node, [])
        
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            
            if neighbor not in visited:
                parents[neighbor] = current_node
                visited.add(neighbor)
                queue.append(neighbor)

    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    shortest_path = []
    
    current_node = destination

    while current_node in parents:
        shortest_path.append(current_node)
        current_node = parents[current_node]

    shortest_path.append(current_node)
    shortest_path.reverse()
    shortest_path.pop()

    return ''.join(shortest_path)


