from graph2 import find_node_by_name, get_coordinates
from reader import time_string_to_int
import heapq
import math


def a_star(graph, start_point, end_point, current_time):
    current_time = time_string_to_int(current_time)
    start = find_node_by_name(graph, start_point)
    end = find_node_by_name(graph, end_point)

    end_lat, end_lon = get_coordinates(end)

    distances = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
    distances[start.name] = current_time

    pq = [(0, current_time, start)]
    prev_nodes = {node.name: None for node_key, node in graph.Nodes.items()}
    while pq:
        _, current_dist, current_node = heapq.heappop(pq)
        if current_node == end:
            # the end
            break
        for neighbor_edge in graph.neighbour_edges(current_node):
            neighbor = find_node_by_name(graph, neighbor_edge.end_node)
            new_time1 = neighbor_edge.departure_time
            new_time2 = neighbor_edge.arrival_time
            if new_time1 >= current_dist:
                # jeśli czas jest dopuszczalny, nie odjeżdża przed naszym przyjazdem
                if new_time2 < distances[neighbor.name]:
                    # jeśli warunek jest lepszy od obecnie zapisanego
                    distances[neighbor.name] = new_time2
                    prev_nodes[neighbor.name] = neighbor_edge
                    heapq.heappush(pq, (calculate_distance(end_lon, end_lat, neighbor_edge.end_stop_lon,
                                                           neighbor_edge.end_stop_lat) +
                                        new_time2, new_time2, neighbor))
    return distances[end_point], prev_nodes


def a_star_the_same_lines(graph, start_point, end_point, current_time):
    current_time = time_string_to_int(current_time)
    start = find_node_by_name(graph, start_point)
    end = find_node_by_name(graph, end_point)

    end_lon, end_lat = get_coordinates(end)

    distances = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
    distances[start.name] = current_time
    distances3 = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
    distances3[start.name] = 0

    pq = [(0, current_time, start, '0')]
    prev_nodes = {node.name: None for node_key, node in graph.Nodes.items()}

    the_line = 0
    while pq:
        _, current_dist, current_node, current_line = heapq.heappop(pq)

        if current_node == end:
            # koniec
            the_line = current_line
            break

        for neighbor_edge in graph.neighbour_edges(current_node):
            neighbor = find_node_by_name(graph, neighbor_edge.end_node)
            new_time1 = neighbor_edge.departure_time
            new_time2 = neighbor_edge.arrival_time
            lat1 = neighbor_edge.end_stop_lat
            lon1 = neighbor_edge.end_stop_lon
            line = neighbor_edge.line

            if new_time1 >= current_dist:
                # jeśli czas jest dopuszczalny, nie odjeżdża przed naszym przyjazdem
                if new_time2 < distances[neighbor.name]:
                    # jeśli warunek jest lepszy od obecnie zapisanego
                    distances[neighbor.name] = new_time2
                    prev_nodes[neighbor.name] = neighbor_edge
                    if current_line == line:
                        heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) / 2,
                                            new_time2, neighbor, line))
                    else:
                        heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) + 86400,
                                            new_time2, neighbor, line))
    # podejście drugie
    distances = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
    distances[start.name] = current_time
    distances3 = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
    distances3[start.name] = 0
    pq = [(0, current_time, start, the_line)]
    prev_nodes = {node.name: None for node_key, node in graph.Nodes.items()}
    while pq:
        current_distance, current_dist, current_node, current_line = heapq.heappop(pq)
        current_node_lon, current_node_lat = get_coordinates(current_node)
        if current_node == end:
            # koniec
            break
        for neighbor_edge in graph.neighbour_edges(current_node):
            neighbor = find_node_by_name(graph, neighbor_edge.end_node)
            new_time1 = neighbor_edge.departure_time
            new_time2 = neighbor_edge.arrival_time
            lat1 = neighbor_edge.end_stop_lat
            lon1 = neighbor_edge.end_stop_lon
            line = neighbor_edge.line

            if new_time1 >= current_dist:
                # jeśli czas jest dopuszczalny, nie odjeżdża przed naszym przyjazdem
                if new_time2 < distances[neighbor.name]:
                    # jeśli warunek jest lepszy od obecnie zapisanego
                    distances[neighbor.name] = new_time2
                    prev_nodes[neighbor.name] = neighbor_edge
                    if line == the_line:
                        heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) / 4,
                                            new_time2, neighbor, line))
                    elif current_line == line:
                        heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) / 2 + 3600,
                                            new_time2, neighbor, line))
                    else:
                        heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) + 86400,
                                            new_time2, neighbor, line))

    return distances[end_point], prev_nodes

# def a_star_the_same_lines(graph, start_point, end_point, current_time):
#     current_time = time_string_to_int(current_time)
#
#     # podejście pierwsze- od końca
#     start = find_node_by_name(graph, end_point)
#     end = find_node_by_name(graph, start_point)
#
#     end_lon, end_lat = get_coordinates(end)
#
#     distances = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
#     distances[start.name] = current_time
#     distances3 = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
#     distances3[start.name] = 0
#
#     pq = [(0, current_time, start, '0')]
#     prev_nodes = {node.name: None for node_key, node in graph.Nodes.items()}
#     while pq:
#         _, current_dist, current_node, current_line = heapq.heappop(pq)
#
#         if current_node == end:
#             # koniec
#             break
#
#         for neighbor_edge in graph.neighbour_edges(current_node):
#             neighbor = find_node_by_name(graph, neighbor_edge.end_node)
#             new_time1 = neighbor_edge.departure_time
#             new_time2 = neighbor_edge.arrival_time
#             lat1 = neighbor_edge.end_stop_lat
#             lon1 = neighbor_edge.end_stop_lon
#             line = neighbor_edge.line
#
#             if new_time1 >= current_dist:
#                 # jeśli czas jest dopuszczalny, nie odjeżdża przed naszym przyjazdem
#                 if new_time2 < distances[neighbor.name]:
#                     # jeśli warunek jest lepszy od obecnie zapisanego
#                     distances[neighbor.name] = new_time2
#                     prev_nodes[neighbor.name] = neighbor_edge
#                     if current_line == line:
#                         heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) / 2,
#                                             new_time2, neighbor, line))
#                     else:
#                         heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) + 86400,
#                                             new_time2, neighbor, line))
#
#     # podejście drugie
#     previous_lines = get_all_lines(prev_nodes, end_point, start_point)
#     start = find_node_by_name(graph, start_point)
#     end = find_node_by_name(graph, end_point)
#
#     end_lon, end_lat = get_coordinates(end)
#
#     distances = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
#     distances[start.name] = current_time
#     distances3 = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
#     distances3[start.name] = 0
#
#     pq = [(0, current_time, start, '0')]
#     prev_nodes = {node.name: None for node_key, node in graph.Nodes.items()}
#
#     the_line = 0
#     while pq:
#         _, current_dist, current_node, current_line = heapq.heappop(pq)
#
#         if current_node == end:
#             # koniec
#             the_line = current_line
#             break
#
#         for neighbor_edge in graph.neighbour_edges(current_node):
#             neighbor = find_node_by_name(graph, neighbor_edge.end_node)
#             new_time1 = neighbor_edge.departure_time
#             new_time2 = neighbor_edge.arrival_time
#             lat1 = neighbor_edge.end_stop_lat
#             lon1 = neighbor_edge.end_stop_lon
#             line = neighbor_edge.line
#
#             if new_time1 >= current_dist:
#                 # jeśli czas jest dopuszczalny, nie odjeżdża przed naszym przyjazdem
#                 if new_time2 < distances[neighbor.name]:
#                     # jeśli warunek jest lepszy od obecnie zapisanego
#                     distances[neighbor.name] = new_time2
#                     prev_nodes[neighbor.name] = neighbor_edge
#                     if line in previous_lines:
#                         heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) / previous_lines[line],
#                                             new_time2, neighbor, line))
#                     if current_line == line:
#                         heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) / 2,
#                                             new_time2, neighbor, line))
#                     else:
#                         heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) + 86400,
#                                             new_time2, neighbor, line))
#
#     # podejście trzecie
#     previous_lines = get_all_lines(prev_nodes, start_point, end_point)
#     distances = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
#     distances[start.name] = current_time
#     distances3 = {node.name: float('inf') for node_key, node in graph.Nodes.items()}
#     distances3[start.name] = 0
#     pq = [(0, current_time, start, the_line)]
#     prev_nodes = {node.name: None for node_key, node in graph.Nodes.items()}
#     while pq:
#         current_distance, current_dist, current_node, current_line = heapq.heappop(pq)
#         current_node_lon, current_node_lat = get_coordinates(current_node)
#         if current_node == end:
#             # koniec
#             break
#         for neighbor_edge in graph.neighbour_edges(current_node):
#             neighbor = find_node_by_name(graph, neighbor_edge.end_node)
#             new_time1 = neighbor_edge.departure_time
#             new_time2 = neighbor_edge.arrival_time
#             lat1 = neighbor_edge.end_stop_lat
#             lon1 = neighbor_edge.end_stop_lon
#             line = neighbor_edge.line
#
#             if new_time1 >= current_dist:
#                 # jeśli czas jest dopuszczalny, nie odjeżdża przed naszym przyjazdem
#                 if new_time2 < distances[neighbor.name] or \
#                         (new_time2 < distances[neighbor.name] + 300 and line == the_line and
#                          calculate_distance(lon1, lat1, end_lon, end_lat) < calculate_distance(lon1, lat1, current_node_lon, current_node_lat)):
#                     # jeśli warunek jest lepszy od obecnie zapisanego
#                     distances[neighbor.name] = new_time2
#                     prev_nodes[neighbor.name] = neighbor_edge
#                     if line == the_line:
#                         heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) / 10,
#                                             new_time2, neighbor, line))
#                     elif line in previous_lines:
#                         heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) / (11 - previous_lines[line]),
#                                             new_time2, neighbor, line))
#                     if current_line == line:
#                         heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) / 2,
#                                             new_time2, neighbor, line))
#                     else:
#                         heapq.heappush(pq, ((calculate_distance(end_lon, end_lat, lon1, lat1) + new_time2) + 86400,
#                                             new_time2, neighbor, line))
#
#     return distances[end_point], prev_nodes


def get_all_lines(prev_nodes, start, end):
    path = []
    current_key = end
    while current_key != start:
        path.append(prev_nodes[current_key].line)
        current_key = prev_nodes[current_key].start_node.name
    path2 = {}
    indicator = 10
    for i in path:
        if i not in path2:
            path2[i] = indicator
            indicator -= 1
    return path2


def calculate_distance(lon1, lat1, lon2, lat2):
    return (2 * math.pi * 6371 * (lon1 - lon2) / 360) ** 2 + (2 * math.pi * 6371 * (lat1 - lat2) / 360) ** 2
