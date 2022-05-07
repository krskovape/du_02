import csv
from datetime import time
from os import stat

download_data = input("Do you want to download and unzip data? (yes/no) ")

if download_data == "yes":
    import get_data
    get_data.retrieve_data()
elif download_data == "no":
    pass
else:
    print("Wrong answear.", input("Try again! (yes/no) "))

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
    def __init__ (self, from_stop, to_stop, trip, route_short_name):
        self.from_stop = from_stop
        self.to_stop = to_stop
        self.trips : list = [trip]
        self.number_of_trips = 1
        self.routes : list = [route_short_name]

stop_file = "gtfs\\stops.txt"
list_stops, dict_stops = Stop.add_element(stop_file)
#print(list_stops)
print(f"Stops: {len(list_stops)}")

routes_file = "gtfs\\routes.txt"
list_routes, dict_routes = Route.add_element(routes_file)
#print(list_routes)
print(f"Routes: {len(list_routes)}")

trips_file = "gtfs\\trips.txt"
list_trips, dict_trips = Trip.add_element(trips_file, dict_routes)
#print(list_trips)
print(f"Trips: {len(list_trips)}")

stop_times_file = "gtfs\\stop_times.txt"
list_stop_times= StopTime.add_element(stop_times_file, dict_trips, dict_stops)
#print(list_stop_times)
print(f"StopTimes: {len(list_stop_times)}")

#stop_segment = StopSegment()
#list_stop_segments = []
dict_stop_segments = {}

i = 0
j = 1

while j <= len(list_stop_times)-1:
    if list_stop_times[i].trip == list_stop_times[j].trip\
        and list_stop_times[i].stop_sequence < list_stop_times[j].stop_sequence:

        if (str(list_stop_times[i].stop.stop_id)+str(list_stop_times[j].stop.stop_id)) in dict_stop_segments:
            dict_stop_segments[str(list_stop_times[i].stop.stop_id)+str(list_stop_times[j].stop.stop_id)].trips.append(list_stop_times[i].trip)
            dict_stop_segments[str(list_stop_times[i].stop.stop_id)+str(list_stop_times[j].stop.stop_id)].number_of_trips += 1
            if list_stop_times[i].trip.route.route_short_name not in dict_stop_segments[str(list_stop_times[i].stop.stop_id)+str(list_stop_times[j].stop.stop_id)].routes:
                dict_stop_segments[str(list_stop_times[i].stop.stop_id)+str(list_stop_times[j].stop.stop_id)].routes.append(list_stop_times[i].trip.route.route_short_name)

        else:
            dict_stop_segments[str(list_stop_times[i].stop.stop_id)+str(list_stop_times[j].stop.stop_id)] = \
                StopSegment(list_stop_times[i].stop, list_stop_times[j].stop, list_stop_times[i].trip, list_stop_times[i].trip.route.route_short_name)
    i += 1
    j += 1

print("\n")

#sorted(dict_stop_segments.items(), key= lambda x: x[x].number_of_trips)
sorted(dict_stop_segments.items(), reverse= True)
print(list(dict_stop_segments.values())[0].routes)
print(list(dict_stop_segments.values())[0].number_of_trips, list(dict_stop_segments.values())[0].from_stop.stop_name, list(dict_stop_segments.values())[0].to_stop.stop_name)
print(list(dict_stop_segments.values())[1].number_of_trips, list(dict_stop_segments.values())[1].from_stop.stop_name, list(dict_stop_segments.values())[1].to_stop.stop_name)
print(list(dict_stop_segments.values())[2].number_of_trips, list(dict_stop_segments.values())[2].from_stop.stop_name, list(dict_stop_segments.values())[2].to_stop.stop_name)
print(list(dict_stop_segments.values())[3].number_of_trips, list(dict_stop_segments.values())[3].from_stop.stop_name, list(dict_stop_segments.values())[3].to_stop.stop_name)
