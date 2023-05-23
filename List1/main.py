import time
import astar
import dijkstra
from graph2 import Graph
from reader import read_csv
import re


def write_final_path(route):
    if route:
        (final_path, last_stop) = dijkstra.decrypt_path(graph, route, start_node, end_node)
        print("Twoja trasa:")
        for stop in final_path:
            print('Wsiadasz na przystanku: ' + str(stop[0]) +
                  ',\to godzinie: ' + str(stop[2]) +
                  '\tw autobus/tramwaj linii: ' + str(stop[1]))
        print('Wysiadasz na przystanku: ' + last_stop[0] + ' o godzinie: ' + str(last_stop[1]))
    else:
        print("Połączenie pomiędzy przystankami nie znalezione.")
    print('\n')


if __name__ == '__main__':
    print("Trwa ładowanie ")

    graph = Graph()
    read_csv(graph)

    # # read input from user
    # while True:  # wczytanie nazwy początkowego przystanku
    #     start_node = input('Podaj przystanek początkowy\n').upper()
    #     if start_node in graph.Nodes:
    #         break
    #     else:
    #         print('Nie ma takiego przystanku')
    # while True:  # wczytanie nazwy końcowego przystanku
    #     end_node = input('Podaj przystanek końcowy\n').upper()
    #     if end_node in graph.Nodes and start_node != end_node:
    #         break
    #     else:
    #         print('Nie ma takiego przystanku lub podany przystanek jest przystankiem początkowym')
    # while True:  # wczytanie czasu dotarcia na przystanek
    #     start_time = input('Podaj czas początkowy(GG:MM)\n')
    #     if re.search("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]", start_time):
    #         start_time += ':00'
    #         break
    # while True:  # wczytanie trybu
    #     time_or_stops = input('Podaj kryterium szukania(c/p):\n').upper()
    #     if time_or_stops == 'C' or time_or_stops == 'P':
    #         break
    #     else:
    #         print('-', time_or_stops, '-')

    # standard data
    start_node = "LEŚNICA".upper()
    end_node = "KSIĘŻE MAŁE".upper()
    start_time = "7:30:00"
    # time_or_stops = 'C'

    # dijkstra
    st = time.time()
    (endTime, path) = dijkstra.dijkstra(graph, start_node, end_node, start_time)
    et = time.time()
    print('Czas wyliczania Dijkstry: ', et - st, 'sekund')
    write_final_path(path)

    # if time_or_stops == 'C':
    # A*
    st = time.time()
    (endTime, path) = astar.a_star(graph, start_node, end_node, start_time)
    et = time.time()
    print('Czas wyliczania A*: ', et - st, 'sekund')
    write_final_path(path)
    # else:
    # A* the same line
    st = time.time()
    (endTime, path) = astar.a_star_the_same_lines(graph, start_node, end_node, start_time)
    et = time.time()
    print('Czas wyliczania A* przy kryterium przesiadek: ', et - st, 'sekund')
    write_final_path(path)
