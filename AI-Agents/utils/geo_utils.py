import requests
import streamlit as st
from config import GRAPHHOPPER_API_KEY

def get_coordinates_graphhopper(city):
    """Get coordinates using the Graphhopper Geocoding API"""
    try:
        url = f"https://graphhopper.com/api/1/geocode"
        params = {
            "q": city,
            "limit": 1,
            "key": GRAPHHOPPER_API_KEY
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        if "hits" in data and data["hits"]:
            point = data["hits"][0]["point"]
            return [point["lng"], point["lat"]]
        
        return None
    except Exception as e:
        st.markdown(f"""
        <div class="status-box error-box">
            <h3>❌ Geocoding Error</h3>
            <p>Error getting coordinates for {city}: {str(e)}</p>
        </div>
        """, unsafe_allow_html=True)
        return None

def get_distance_graphhopper(city1, city2):
    """Get road distance using the Graphhopper Routing API"""
    try:
        city1_coords = get_coordinates_graphhopper(city1)
        city2_coords = get_coordinates_graphhopper(city2)
        
        if not city1_coords or not city2_coords:
            return None
            
        url = "https://graphhopper.com/api/1/route"
        params = {
            "point": [f"{city1_coords[1]},{city1_coords[0]}", f"{city2_coords[1]},{city2_coords[0]}"],
            "vehicle": "car",
            "key": GRAPHHOPPER_API_KEY
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        if "paths" in data and data["paths"]:
            distance_m = data["paths"][0]["distance"]
            return distance_m / 1000
            
        return None
    except Exception as e:
        st.markdown(f"""
        <div class="status-box error-box">
            <h3>❌ Routing Error</h3>
            <p>Error fetching road distance: {str(e)}</p>
        </div>
        """, unsafe_allow_html=True)
        return None