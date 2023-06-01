import pandas as pd
from datetime import datetime
from Edge import Edge
from graph2 import find_node_by_name


def read_csv(graph):
    df = pd.read_csv('connection_graph.csv')
    for index, row in df.iterrows():
        company = row[2]
        travel_line = row[3]
        departure_time = row[4]
        arrival_time = row[5]
        start_stop = row[6].upper()
        end_stop = row[7].upper()
        start_stop_lat = row[8]
        start_stop_lon = row[9]
        end_stop_lat = row[10]
        end_stop_lon = row[11]

        graph.add_node(start_stop)
        graph.add_node(end_stop)

        edge = Edge(company, travel_line, time_string_to_int(arrival_time),
                    time_string_to_int(departure_time), find_node_by_name(graph, start_stop),
                    end_stop, start_stop_lat, start_stop_lon, end_stop_lat, end_stop_lon)
        graph.add_edge(edge)
    print("dane załadowane")


def time_string_to_int(time_string):
    time_obj = datetime.strptime(time_string, "%H:%M:%S").time()
    str_time = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

    return str_time
