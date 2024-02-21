import heapq 

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 5},
    'C': {'D': 2}
}

def heuristic(node, goal):
    heuristic_values = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 0
    }
    return heuristic_values[node]

def ao_star(start, goal):
    opened = [(0, start)]
    heapq.heapify(opened) 
    
    g_scores = {start: 0}
    came_from = {} 
    
    while opened:
        g_cost, current = heapq.heappop(opened)
        
        if current == goal:
            return reconstruct_path(came_from, current)
            
        for neighbor, move_cost in graph[current].items():
            tentative_g = g_scores[current] + move_cost

            if tentative_g < g_scores.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(opened, (f, neighbor))
                
    return None

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    return path[::-1]

start = 'A' 
goal = 'D'

path = ao_star(start, goal)
print("Shortest Path:", path)
