class Edge:
    def __init__(self, company, line, arrival_time, departure_time, start_node, end_node,
                 start_stop_lat, start_stop_lon, end_stop_lat, end_stop_lon):
        # self.id = id
        self.company = company
        self.line = line
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.start_node = start_node
        self.end_node = end_node
        self.start_stop_lat = start_stop_lat
        self.start_stop_lon = start_stop_lon
        self.end_stop_lat = end_stop_lat
        self.end_stop_lon = end_stop_lon
