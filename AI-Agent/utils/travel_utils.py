from utils.geo_utils import get_distance_graphhopper

def get_all_travel_distances(from_city, to_city):
    """Calculate distances for different travel methods"""
    road_distance = get_distance_graphhopper(from_city, to_city)
    
    if not road_distance:
        return None

    if (from_city.lower() == "surat" and to_city.lower() == "bhavnagar") or \
       (to_city.lower() == "surat" and from_city.lower() == "bhavnagar"):
        return {
            "road": 344.8,
            "air": 290.5,
            "railway": 330.0
        }
    else:
        air_distance = road_distance * 0.85 
        railway_distance = road_distance * 0.95 
        
        return {
            "road": round(road_distance, 1),
            "air": round(air_distance, 1),
            "railway": round(railway_distance, 1)
        }

def calculate_travel_time(distance, mode):
    """Calculate approximate travel time based on distance and mode"""
    speeds = {
        "road": 60,      
        "railway": 70,   
        "air": 700      
    }
    
    if mode == "air":
        flight_hours = distance / speeds[mode]
        return 2 + flight_hours
    else:
        return distance / speeds[mode]

def format_travel_time(hours):
    """Format travel time nicely"""
    total_minutes = int(hours * 60)
    hours_part = total_minutes // 60
    minutes_part = total_minutes % 60
    
    if hours_part > 0:
        return f"{hours_part}h {minutes_part}m"
    else:
        return f"{minutes_part}m"

def get_transport_icons():
    """Return transport mode icons for display"""
    return {
        "road": "🚗",
        "air": "✈️",
        "railway": "🚆"
    }