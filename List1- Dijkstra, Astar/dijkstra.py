import heapq
from graph2 import find_node_by_name
from reader import time_string_to_int


def dijkstra(graph, start_point, end_point, current_time):
    current_time = time_string_to_int(current_time)
    start = find_node_by_name(graph, start_point)
    end = find_node_by_name(graph, end_point)

    distances = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
    distances[start.name] = current_time
    pq = [(current_time, start)]
    prev_nodes = {node.name: None for node_key, node in graph.Nodes.items()}
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node == end:
            # koniec
            break
        for neighbor_edge in graph.neighbour_edges(current_node):
            neighbor = find_node_by_name(graph, neighbor_edge.end_node)
            new_time1 = neighbor_edge.departure_time
            new_time2 = neighbor_edge.arrival_time
            if new_time1 >= current_dist:
                # jeśli czas jest dopuszczalny, nie odjeżdża przed naszym przyjazdem
                if new_time2 < distances[neighbor.name]:
                    # jeśli czas jest lepszy od obecnie zapisanego
                    distances[neighbor.name] = new_time2
                    prev_nodes[neighbor.name] = neighbor_edge
                    heapq.heappush(pq, (new_time2, neighbor))

    return distances[end_point], prev_nodes


def decrypt_path(graph, shortest_paths, start, end):
    path = []
    current_key = end
    while current_key != start:
        path.append((shortest_paths[current_key].start_node, shortest_paths[current_key].line,
                     shortest_paths[current_key].departure_time))
        current_key = shortest_paths[current_key].start_node.name

    last_stop = (end, time_int_to_string(shortest_paths[end].arrival_time))
    path = path[::-1]
    path2 = []
    line = path[0][1]

    for i in path:
        if i[1] != line:
            path2.append((i[0].name, i[1], time_int_to_string(i[2])))
            line = i[1]
    return path2, last_stop


def time_int_to_string(int_time):
    str_time = str(int(int_time / 3600)) + ':' + str((int(int_time / 60)) % 60) + ':' + str(int(int_time) % 60)
    return str_time
