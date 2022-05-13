import csv
from datetime import time
from ntpath import join
import os
from turtle import down

# download_data = input("Chcete stáhnout a rozbalit data? (ano/ne) ")

# if download_data == "ano":
#     import get_data
#     get_data.retrieve_data()
# elif download_data == "ne":
#     pass
# else:
#     print("Chybná odpověď.", input("Zkuste to znovu! (ano/ne) "))
#     # print("Chybná odpověď. Program skončí.")
#     # quit()

download_data = None

while download_data not in ("ano", "ne"): 
    download_data = input("Chcete stáhnout a rozbalit data? (ano/ne) ")
    if download_data == "ne": 
        print("Program se spustí na Vašich datech. Pokud neexistují, skončí.")
        continue
    if download_data == "ano":
        import get_data
        get_data.retrieve_data()
    else: 
        print("Chybná odpověď. Zkuste to znovu!") 


class GTFSTable():
    def __init__(self) -> None:
        pass

    def load_file(self, file_name):
        try:
            with open(file_name, encoding="utf-8", newline = '') as csvfile:
                #empty file
                if os.stat(file_name).st_size == 0:
                    print("Složka je prázdná.")
                    quit()
                
                dict_reader = csv.DictReader(csvfile, delimiter = ',')

                alist = []
                for feature in dict_reader:
                    alist.append(feature)
                return alist

        except FileNotFoundError:
            print(f"Nelze otevřít soubor {file_name}. Soubor neexistuje nebo je k němu zadána nekorektní cesta")
            quit()
        except PermissionError:
            print(f"Program nemá povolen přístup k souboru {file_name}.")
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
    def elements_from_file(cls, file_name):
        alist = cls.load_file(cls, file_name)
        dict_stops = {}
        list_stop = []
        for item in alist:
            stop_object = cls(item)
            dict_stops[item["stop_id"]] = stop_object
            list_stop.append(stop_object)
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
    def elements_from_file(cls, file_name, dict_trips, dict_stops):
        alist = cls.load_file(cls, file_name)
        list_stop_times = []
        for item in alist:
            stop_time_object = cls(item, dict_trips, dict_stops)
            list_stop_times.append(stop_time_object)
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
    def elements_from_file(cls, file_name, dict_routes):
        alist = cls.load_file(cls, file_name)
        dict_trips = {}
        list_trips = []
        for item in alist:
            trip_object = cls(item, dict_routes)
            dict_trips[item["trip_id"]] = trip_object
            list_trips.append(trip_object)
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
    def elements_from_file(cls, file_name):
        alist = cls.load_file(cls, file_name)
        dict_routes = {}
        list_routes = []
        for item in alist:
            route_object = cls(item)
            dict_routes[item["route_id"]] = route_object
            list_routes.append(route_object)
        return list_routes, dict_routes
    
    

class StopSegment(GTFSTable):
    def __init__ (self, from_stop, to_stop, trip, route_short_name):
        self.from_stop = from_stop
        self.to_stop = to_stop
        self.trips : list = [trip]
        self.number_of_trips = 1
        self.routes : list = [route_short_name]
    
    @classmethod
    def create_segments(cls, list_stop_times):
        dict_stop_segments = {}

        j = 1

        #while j <= len(list_stop_times)-1:
        for j in range(len(list_stop_times)-1):
            st_from = list_stop_times[j-1]
            st_to = list_stop_times[j]
            if st_from.trip == st_to.trip\
                and st_from.stop_sequence < st_to.stop_sequence:

                if ((st_from.stop.stop_id),(st_to.stop.stop_id)) in dict_stop_segments:
                    dict_stop_segments[((st_from.stop.stop_id),(st_to.stop.stop_id))].trips.append(st_from.trip)
                    dict_stop_segments[((st_from.stop.stop_id),(st_to.stop.stop_id))].number_of_trips += 1
                    if st_from.trip.route.route_short_name not in dict_stop_segments[((st_from.stop.stop_id),(st_to.stop.stop_id))].routes:
                        dict_stop_segments[((st_from.stop.stop_id),(st_to.stop.stop_id))].routes.append(st_from.trip.route.route_short_name)

                else:
                    dict_stop_segments[((st_from.stop.stop_id),(st_to.stop.stop_id))] = \
                        cls(st_from.stop, st_to.stop, st_from.trip, st_from.trip.route.route_short_name)
            j += 1
        
        return dict_stop_segments
        

#print("Počet objektů:")
stop_file = os.path.join("gtfs", "stops.txt")
list_stops, dict_stops = Stop.elements_from_file(stop_file)
#print(f"Stops: {len(list_stops)}")

routes_file = os.path.join("gtfs", "routes.txt")
list_routes, dict_routes = Route.elements_from_file(routes_file)
#print(f"Routes: {len(list_routes)}")

trips_file = os.path.join("gtfs", "trips.txt")
list_trips, dict_trips = Trip.elements_from_file(trips_file, dict_routes)
#print(f"Trips: {len(list_trips)}")

stop_times_file = os.path.join("gtfs", "stop_times.txt")
list_stop_times= StopTime.elements_from_file(stop_times_file, dict_trips, dict_stops)
#print(f"StopTimes: {len(list_stop_times)}")

print("\n")

dict_stop_segments = StopSegment.create_segments(list_stop_times)
segments_sorted = sorted(dict_stop_segments.values(), key= lambda x: x.number_of_trips, reverse= True)

print("Nejfrekventovanější mezizastávkové úseky:")
print(f"1: {segments_sorted[0].from_stop.stop_name} - {segments_sorted[0].to_stop.stop_name}, počet spojů: {segments_sorted[0].number_of_trips}, linky: {' '.join(sorted(segments_sorted[0].routes, key = int))}")
print(f"2: {segments_sorted[1].from_stop.stop_name} - {segments_sorted[1].to_stop.stop_name}, počet spojů: {segments_sorted[1].number_of_trips}, linky: {' '.join(sorted(segments_sorted[1].routes, key = int))}")
print(f"3: {segments_sorted[2].from_stop.stop_name} - {segments_sorted[2].to_stop.stop_name}, počet spojů: {segments_sorted[2].number_of_trips}, linky: {' '.join(sorted(segments_sorted[2].routes, key = int))}")
print(f"4: {segments_sorted[3].from_stop.stop_name} - {segments_sorted[3].to_stop.stop_name}, počet spojů: {segments_sorted[3].number_of_trips}, linky: {' '.join(sorted(segments_sorted[3].routes, key = int))}")
print(f"5: {segments_sorted[4].from_stop.stop_name} - {segments_sorted[4].to_stop.stop_name}, počet spojů: {segments_sorted[4].number_of_trips}, linky: {' '.join(sorted(segments_sorted[4].routes, key = int))}")
