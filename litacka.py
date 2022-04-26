import csv
from os import stat

def open_file(file_name):
    try:
        with open(file_name, encoding="utf-8", newline = ',') as csvfile:
            if stat(file_name).st_size == 0:
                print("File is empty.")
                quit()
            return csv.DictReader(csvfile)
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to access file {file_name}.")
        quit()

class Stops():
    def __init__(self):
        data = open_file("stops.txt")
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

class StopTimes():
    def __init__(self):
        #data = co nám vrátí funkce načítání z texťáku přes DictReader
        data = open_file("stop_times.txt")
        self.trip_id = data["trip_id"]
        self.arrival_time = data["arrival_time"]
        self.departure_time = data["departure_time"]
        self.stop_id = data["stop_id"]
        self.stop_sequence = data["stop_sequence"]
        self.stop_headsign = data["stop_headsign"]
        self.pickup_type = data["pickup_type"]
        self.drop_off_type = ["drop_off_type"]
        self.shape_dist_traveled = data["shape_dist_traveled"]
        self.trip_operation_type = ["trip_operation_type"]
        self.bikes_allowed = ["bikes_allowed"]

class Trips ():
    def __init__(self):
        data = open_file("trips.txt")
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
    

class Routes():
    def __init__(self):
        data = open_file("routes.txt")
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