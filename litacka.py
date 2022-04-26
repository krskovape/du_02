#tady bude funkce na otvírání dat...plus minus:
#with open("neco.csv", encoding="utf-8") as csvfile:

class Stops():
    def __init__(self, data):
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
    def __init__(self, data):
        #data = co nám vrátí funkce načítání z texťáku přes DictReader
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
    def __init__(self, data):
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
    def __init__(self, data):
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
        self.trips = None
        self.routes = None
