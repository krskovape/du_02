import csv
from os import stat

class Stops():
    def __init__(self):
        self.stop_id = None
        self.stop_name = None
        self.stop_lat = None
        self.stop_lon = None
        self.zone_id = None
        self.stop_url = None   
        self.location_type = None  
        self.parent_station = None
        self.wheelchair_boarding = None
        self.level_id = None
        self.platform_code = None
        self.asw_node_id = None
        self.asw_stop_id = None
    
    def load(self, data):
        self.stop_id = data["stop_id"]
        self.stop_name = data["stop_name"]
        self.stop_lat = data["stop_lat"]
        self.stop_lon = data["stop_lon"]
        self.zone_id = data["zone_id"]
        self.stop_url = data["stop_url"]   
        self.location_type = data["location_type"]   
        self.parent_station = data["parent_station"]
        self.wheelchair_boarding = data["wheelchair_boarding"]
        self.level_id = data["level_id"]
        self.platform_code = data["platform_code"]
        self.asw_node_id = data["asw_node_id"]
        self.asw_stop_id = data["asw_stop_id"]
    
    def open_file(self, file_name):
        try:
            with open(file_name, encoding="utf-8", newline = '') as csvfile:
                if stat(file_name).st_size == 0:
                    print("File is empty.")
                    quit()
                a = csv.DictReader(csvfile, delimiter = ',')
                for feature in a:
                    self.load(feature)
                    #print(feature)
                return a
        except FileNotFoundError:
            print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
            quit()
        except PermissionError:
            print(f"Program doesn't have permisson to access file {file_name}.")
            quit()

class StopTimes():
    def __init__(self):
        self.trip_id = None
        self.arrival_time = None
        self.departure_time = None
        self.stop_id = None
        self.stop_sequence = None
        self.stop_headsign = None
        self.pickup_type = None
        self.drop_off_type = None
        self.shape_dist_traveled = None
        self.trip_operation_type = None
        self.bikes_allowed = None
    
    def load(self, data):
        self.trip_id = data["trip_id"]
        self.arrival_time = data["arrival_time"]
        self.departure_time = data["departure_time"]
        self.stop_id = data["stop_id"]
        self.stop_sequence = data["stop_sequence"]
        self.stop_headsign = data["stop_headsign"]
        self.pickup_type = data["pickup_type"]
        self.drop_off_type = data["drop_off_type"]
        self.shape_dist_traveled = data["shape_dist_traveled"]
        self.trip_operation_type = data["trip_operation_type"]
        self.bikes_allowed = data["bikes_allowed"]

    def open_file(self, file_name):
        try:
            with open(file_name, encoding="utf-8", newline = '') as csvfile:
                if stat(file_name).st_size == 0:
                    print("File is empty.")
                    quit()
                a = csv.DictReader(csvfile, delimiter = ',')
                trip_indexy = []
                for feature in a:
                    self.load(feature)
                    trip_indexy.append(feature["trip_id"])
                    #print(feature)
                return trip_indexy
        except FileNotFoundError:
            print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
            quit()
        except PermissionError:
            print(f"Program doesn't have permisson to access file {file_name}.")
            quit()

class Trips():
    def __init__(self):
        self.route_id = None
        self.service_id = None
        self.trip_id = None
        self.trip_headsign = None
        self.trip_short_name = None
        self.direction_id = None
        self.block_id = None
        self.shape_id = None
        self.wheelchair_accessible = None
        self.bikes_allowed = None
        self.exceptional = None
    
    def load(self, data):
        self.route_id = data["route_id"]
        self.service_id = data["service_id"]
        self.trip_id = data["trip_id"]
        self.trip_headsign = data["trip_headsign"]
        self.trip_short_name = data["trip_short_name"]
        self.direction_id = data["direction_id"]
        self.block_id = data["block_id"]
        self.shape_id = data["shape_id"]
        self.wheelchair_accessible = data["wheelchair_accessible"]
        self.bikes_allowed = data["bikes_allowed"]
        self.exceptional = ["exceptional"]
    
    def open_file(self, file_name):
        try:
            with open(file_name, encoding="utf-8", newline = '') as csvfile:
                if stat(file_name).st_size == 0:
                    print("File is empty.")
                    quit()
                a = csv.DictReader(csvfile, delimiter = ',')
                for feature in a:
                    self.load(feature)
                    #print(feature)
                return a
        except FileNotFoundError:
            print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
            quit()
        except PermissionError:
            print(f"Program doesn't have permisson to access file {file_name}.")
            quit()
    

class Routes():
    def __init__(self):
        self.route_id = None
        self.agency_id = None
        self.route_short_name = None
        self.route_long_name = None
        self.route_type = None
        self.route_url = None
        self.route_color = None
        self.route_text_color = None
        self.is_night = None
        self.is_regional = None
        self.is_substitute_transport = None

    def load(self, data):
        self.route_id = data["route_id"]
        self.agency_id = data["agency_id"]
        self.route_short_name = data["route_short_name"]
        self.route_long_name = data["route_long_name"]
        self.route_type = data["route_type"]
        self.route_url = data["route_url"]
        self.route_color = data["route_color"]
        self.route_text_color = data["route_text_color"]
        self.is_night = data["is_night"]
        self.is_regional = data["is_regional"]
        self.is_substitute_transport = data["is_substitute_transport"]
    
    def open_file(self, file_name):
        try:
            with open(file_name, encoding="utf-8", newline = '') as csvfile:
                if stat(file_name).st_size == 0:
                    print("File is empty.")
                    quit()
                a = csv.DictReader(csvfile, delimiter = ',')
                for feature in a:
                    self.load(feature)
                    #print(feature)
                return a
        except FileNotFoundError:
            print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
            quit()
        except PermissionError:
            print(f"Program doesn't have permisson to access file {file_name}.")
            quit()

class StopSegment():
    def __init__(self):
        self.from_stop = None
        self.to_stop = None
        self.trips = []
        self.number_of_trips = 0
        self.routes = []
    
    #vytvoření segmentu 
    def create (self, from_stop, to_stop, trip_id, route_short_name):
        self.from_stop = from_stop
        self.to_stop = to_stop
        self.trips.append(trip_id)
        self.number_of_trips = 1
        self.routes.append(route_short_name)
    
    def add (self, trip_id, route_short_name):
        self.trips.append(trip_id)
        self.number_of_trips += 1
        if route_short_name not in self.routes:
            self.routes.append(route_short_name)

routes = Routes()
routes_file = "routes.txt"
routes.open_file(routes_file)

stops = Stops()
stops_file = "stops.txt"
stops.open_file(stops_file)

stop_times = StopTimes()
stop_times_file = "stop_times.txt"
trip_indexy = stop_times.open_file(stop_times_file)

trips = Trips()
trips_file = "trips.txt"
trips.open_file(trips_file)

stop_segment = StopSegment()

#vytváření mezizastávkových segmentů
a = 0
while a < len(trip_indexy)-1:
    from_stop = 1
    to_stop = 2
    trip_idx = trip_indexy[a] #trip_id prvního objektu
    segment_from = stop_times.stop_sequence

    while trip_idx == stop_times.trip_id:
        if stop_times.trip_id == trips.trip_id\
            and trips.route_id == routes.route_id:
            route = routes.route_short_name

        # while from_stop != segment_from:
        #     segment_from : StopTimes = segment_from.stop_sequence
        if from_stop == stop_times.stop_sequence:
            segment_from : StopTimes = stop_times.stop_sequence

        if to_stop == stop_times.stop_sequence:
            segment_to : StopTimes = stop_times.stop_sequence

        if stop_segment.from_stop != segment_from.stop_id\
            and stop_segment.to_stop != segment_to.stop_id:
            stop_segment.create(segment_from.stop_id, segment_to.stop_id, trip_idx, route)
        else:
            stop_segment.add(trip_idx, route)

        from_stop = to_stop
        to_stop += 1

    a += 1 #posunout se na další trip_id