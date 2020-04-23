import heapq
import math
from helpers import Map, load_map, show_map


def shortest_path(M, start, goal):
    came_from = {}
    cost = {}
    # Start values
    came_from[start] = None
    cost[start] = 0
    # heapq frontier
    frontier = [(0, start)]

    while len(frontier) > 0:
        node = heapq.heappop(frontier)[1]

        if node == goal:
            break

        for neighbor in M.roads[node]:
            # Get distance of current neighbor
            path_cost = distance(M.intersections[node], M.intersections[neighbor])
            # Add
            current_cost = cost[node] + path_cost 

            if neighbor not in cost or current_cost < cost[neighbor]:
                cost[neighbor] = current_cost
                heuristic = distance(M.intersections[neighbor], M.intersections[goal])
                total_cost = current_cost + heuristic
                came_from[neighbor] = node
                # Heappush cost and neighbor
                heapq.heappush(frontier, (total_cost, neighbor))

    return arrange_route(came_from, start, goal)

# Euclidean distance between nodes
def distance(start, end):
    # path cost is distance between two points
    return math.sqrt(((start[0] - end[0]) ** 2) + ((start[1] - end[1]) ** 2))


def arrange_route(came_from, start, goal):
    # traverse backwards to find optimal path
    node = goal
    path = []
    
    if node not in came_from:
        print("Node: {} not found in map.".format(node))
        return

    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()
    print(path)
    return path


# test maps
map_10 = load_map("map-10.pickle")
map_40 = load_map("map-40.pickle")

# Test 1
shortest_path(map_40, 8, 24)  # path: [8, 14, 16, 37, 12, 17, 10, 24]
# Test 2
shortest_path(map_10, 2, 0)  # path: [2, 3, 5, 0]
# Test 3
shortest_path(map_10, 3, 9)  # There is no node 9 in map_10
# Test 4
shortest_path(map_40, 5, 34) # path: [5, 16, 37, 12, 34]
# Test 5
shortest_path(map_40, 5, 5)  # path: [5]
