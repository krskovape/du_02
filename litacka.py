import csv
from datetime import time
from os import stat

class GTFSTable():
    def __init__(self) -> None:
        pass

    def load_file(self, file_name):
        try:
            with open(file_name, encoding="utf-8", newline = '') as csvfile:
                #empty file
                if stat(file_name).st_size == 0:
                    print("File is empty.")
                    quit()
                
                a = csv.DictReader(csvfile, delimiter = ',')

                list = []
                for feature in a:
                    list.append(feature)
                return list

        except FileNotFoundError:
            print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
            quit()
        except PermissionError:
            print(f"Program doesn't have permisson to access file {file_name}.")
            quit()

class Stop(GTFSTable):
    def __init__(self, data):
        self.stop_id : str = data["stop_id"]
        self.stop_name : str = data["stop_name"]
        self.stop_lat : float = data["stop_lat"]
        self.stop_lon : float = data["stop_lon"]
        self.zone_id : str = data["zone_id"]
        self.stop_url : str = data["stop_url"]   
        self.location_type : int = data["location_type"]  
        self.parent_station : str = data["parent_station"]
        self.wheelchair_boarding : int = data["wheelchair_boarding"]
        self.level_id : str = data["level_id"]
        self.platform_code : str = data["platform_code"]
        self.asw_node_id : int = data["asw_node_id"]
        self.asw_stop_id : int = data["asw_stop_id"]

    @classmethod
    def add_element(cls, file_name):
        list = cls.load_file(cls, file_name)
        dict_stops = {}
        list_stop = []
        for b in list:
            a = cls(b)
            dict_stops[b["stop_id"]] = a
            list_stop.append(a)
        return list_stop, dict_stops


class StopTime(GTFSTable):
    def __init__(self, data, dict_trips : dict, dict_stops : dict):
        self.trip : Trip = dict_trips.get(data["trip_id"])
        self.arrival_time : time = data["arrival_time"]
        self.departure_time : time = data["departure_time"]
        self.stop : Stop = dict_stops.get(data["stop_id"])
        self.stop_sequence : int = data["stop_sequence"]
        self.stop_headsign : str = data["stop_headsign"]
        self.pickup_type : int = data["pickup_type"]
        self.drop_off_type : int = data["drop_off_type"]
        self.shape_dist_traveled : float = data["shape_dist_traveled"]
        self.trip_operation_type : int = data["trip_operation_type"]
        self.bikes_allowed : int = data["bikes_allowed"]
    
    @classmethod
    def add_element(cls, file_name, dict_trips, dict_stops):
        list = cls.load_file(cls, file_name)
        list_stop_times = []
        for b in list:
            a = cls(b, dict_trips, dict_stops)
            list_stop_times.append(a)
        return list_stop_times


class Trip(GTFSTable):
    def __init__(self, data, dict_routes : dict):
        self.route : Route = dict_routes.get(data["route_id"])
        self.service_id : str = data["service_id"]
        self.trip_id : str = data["trip_id"]
        self.trip_headsign : str = data["trip_headsign"]
        self.trip_short_name : str = data["trip_short_name"]
        self.direction_id : int = data["direction_id"]
        self.block_id : str = data["block_id"]
        self.shape_id : str = data["shape_id"]
        self.wheelchair_accessible : int = data["wheelchair_accessible"]
        self.bikes_allowed : int = data["bikes_allowed"]
        self.exceptional : int = data["exceptional"]
    
    @classmethod
    def add_element(cls, file_name, dict_routes):
        list = cls.load_file(cls, file_name)
        dict_trips = {}
        list_trips = []
        for b in list:
            a = cls(b, dict_routes)
            dict_trips[b["trip_id"]] = a
            list_trips.append(a)
        return list_trips, dict_trips
    

class Route(GTFSTable):
    def __init__(self, data):
        self.route_id : str = data["route_id"]
        self.agency_id = data["agency_id"]
        self.route_short_name : str = data["route_short_name"]
        self.route_long_name : str = data["route_long_name"]
        self.route_type : int = data["route_type"]
        self.route_url : str = data["route_url"]
        self.route_color : str = data["route_color"]
        self.route_text_color : str = data["route_text_color"]
        self.is_night : int = data["is_night"]
        self.is_regional : int = data["is_regional"]
        self.is_substitute_transport : int = data["is_substitute_transport"]
    
    @classmethod
    def add_element(cls, file_name):
        list = cls.load_file(cls, file_name)
        dict_routes = {}
        list_routes = []
        for b in list:
            a = cls(b)
            dict_routes[b["route_id"]] = a
            list_routes.append(a)
        return list_routes, dict_routes
    
    

class StopSegment(GTFSTable):
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

stop_file = "stops.txt"
list_stops, dict_stops = Stop.add_element(stop_file)
#print(list_stops)
print(len(list_stops))

routes_file = "routes.txt"
list_routes, dict_routes = Route.add_element(routes_file)
#print(list_routes)
print(len(list_routes))

trips_file = "trips.txt"
list_trips, dict_trips = Trip.add_element(trips_file, dict_routes)
#print(list_trips)
print(len(list_trips))

stop_times_file = "stop_times.txt"
list_stop_times= StopTime.add_element(stop_times_file, dict_trips, dict_stops)
#print(list_stop_times)
print(len(list_stop_times))

stop_segment = StopSegment()

#vytváření mezizastávkových segmentů
# a = 0
# while a < len(trip_indexy)-1:
#     from_stop = 1
#     to_stop = 2
#     trip_idx = trip_indexy[a] #trip_id prvního objektu
#     segment_from = stop_time.stop_sequence

#     while trip_idx == stop_time.trip_id:
#         if stop_time.trip_id == trip.trip_id\
#             and trip.route_id == route.route_id:
#             route = route.route_short_name

#         # while from_stop != segment_from:
#         #     segment_from : StopTimes = segment_from.stop_sequence
#         if from_stop == stop_time.stop_sequence:
#             segment_from : StopTime = stop_time.stop_sequence

#         if to_stop == stop_time.stop_sequence:
#             segment_to : StopTime = stop_time.stop_sequence

#         if stop_segment.from_stop != segment_from.stop_id\
#             and stop_segment.to_stop != segment_to.stop_id:
#             stop_segment.create(segment_from.stop_id, segment_to.stop_id, trip_idx, route)
#         else:
#             stop_segment.add(trip_idx, route)

#         from_stop = to_stop
#         to_stop += 1

#     a += 1 #posunout se na další trip_id