import streamlit as st
import json
import re
from utils.travel_utils import calculate_travel_time, format_travel_time, get_transport_icons

def display_travel_info(user_city, city, travel_mode, distances):
    """Display travel information between cities"""
    selected_distance = distances[travel_mode]
    travel_time = calculate_travel_time(selected_distance, travel_mode)
    time_str = format_travel_time(travel_time)

    st.markdown('<h2 class="sub-header">🗺️ Travel Information</h2>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card travel-card-selected">
        <div class="travel-mode-title">
            {get_transport_icons()[travel_mode]}
            <span>Traveling by {travel_mode.capitalize()}</span>
        </div>
        <div class="travel-stat">
            <span>From:</span> 
            <span class="travel-value">{user_city}</span> 
            <span>To:</span> 
            <span class="travel-value">{city}</span>
        </div>
        <div class="travel-stat">
            <span>Distance:</span> 
            <span class="travel-value">{selected_distance} km</span>
        </div>
        <div class="travel-stat">
            <span>Estimated Travel Time:</span> 
            <span class="travel-value">{time_str}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Compare All Travel Options")

    col1, col2, col3 = st.columns(3)

    with col1:
        road_time = calculate_travel_time(distances['road'], 'road')
        road_time_str = format_travel_time(road_time)
        
        st.markdown(f"""
        <div class="card {'travel-card-selected' if travel_mode == 'road' else 'travel-card'}">
            <h4 style="text-align: center;">{get_transport_icons()['road']} Road</h4>
            <div class="travel-stat">Distance: <span class="travel-value">{distances['road']} km</span></div>
            <div class="travel-stat">Time: <span class="travel-value">{road_time_str}</span></div>
            {'<div style="text-align: center; margin-top: 0.5rem;"><span style="background-color: #1E88E5; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8rem;">SELECTED</span></div>' if travel_mode == 'road' else ''}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        air_time = calculate_travel_time(distances['air'], 'air')
        air_time_str = format_travel_time(air_time)
        
        st.markdown(f"""
        <div class="card {'travel-card-selected' if travel_mode == 'air' else 'travel-card'}">
            <h4 style="text-align: center;">{get_transport_icons()['air']} Air</h4>
            <div class="travel-stat">Distance: <span class="travel-value">{distances['air']} km</span></div>
            <div class="travel-stat">Time: <span class="travel-value">{air_time_str}</span></div>
            {'<div style="text-align: center; margin-top: 0.5rem;"><span style="background-color: #1E88E5; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8rem;">SELECTED</span></div>' if travel_mode == 'air' else ''}
        </div>
        """, unsafe_allow_html=True)

    with col3:
        rail_time = calculate_travel_time(distances['railway'], 'railway')
        rail_time_str = format_travel_time(rail_time)
        
        st.markdown(f"""
        <div class="card {'travel-card-selected' if travel_mode == 'railway' else 'travel-card'}">
            <h4 style="text-align: center;">{get_transport_icons()['railway']} Railway</h4>
            <div class="travel-stat">Distance: <span class="travel-value">{distances['railway']} km</span></div>
            <div class="travel-stat">Time: <span class="travel-value">{rail_time_str}</span></div>
            {'<div style="text-align: center; margin-top: 0.5rem;"><span style="background-color: #1E88E5; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8rem;">SELECTED</span></div>' if travel_mode == 'railway' else ''}
        </div>
        """, unsafe_allow_html=True)

def display_hotel_results(hotels, nights, check_in, check_out, travel_mode):
    """Display hotel search results"""
    if not hotels:
        st.markdown("""
        <div class="status-box warning-box">
            <h3>⚠️ No Hotel Data</h3>
            <p>No hotel data could be extracted. Please try again or modify your search.</p>
        </div>
        """, unsafe_allow_html=True)
        return

    for hotel in hotels:
        hotel['total_cost'] = hotel.get('price', 0) * nights

    st.markdown('<h2 class="sub-header">🏨 Recommended Hotels</h2>', unsafe_allow_html=True)

    sorted_hotels = sorted(hotels, key=lambda x: float(x.get('rating', 0)), reverse=True)

    col1, col2 = st.columns(2)
    
    for i, hotel in enumerate(sorted_hotels):
        with (col1 if i % 2 == 0 else col2):
            rating = float(hotel.get('rating', 0))
            stars = "⭐" * int(rating) + ("½" if rating % 1 >= 0.5 else "")
            
            st.markdown(f"""
            <div class="card hotel-card">
                <div class="hotel-name">🏨 {hotel.get('name', 'Unknown Hotel')}</div>
                <div class="hotel-detail">📍 {hotel.get('location', 'N/A')}</div>
                <div class="hotel-detail">{stars} {hotel.get('rating', 'N/A')}/5</div>
                <div class="hotel-detail">💰 ₹{hotel.get('price', 'N/A')}/night</div>
                <div class="hotel-detail">💵 Total: ₹{hotel.get('total_cost', 'N/A')} for {nights} night{'s' if nights > 1 else ''}</div>
                <div class="hotel-detail">📅 {check_in.strftime("%d %b")} - {check_out.strftime("%d %b")}</div>
                <div class="hotel-detail">{get_transport_icons()[travel_mode]} Arriving by {travel_mode.capitalize()}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<h3 class="sub-header">📋 Hotel Comparison</h3>', unsafe_allow_html=True)

    comparison_data = []
    for hotel in sorted_hotels:
        comparison_data.append({
            "Name": hotel.get('name', 'Unknown'),
            "Location": hotel.get('location', 'N/A'),
            "Rating": hotel.get('rating', 'N/A'),
            "Price/Night": f"₹{hotel.get('price', 'N/A')}",
            "Total Cost": f"₹{hotel.get('total_cost', 'N/A')}"
        })
    
    st.dataframe(
        comparison_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Name": st.column_config.TextColumn("Hotel Name"),
            "Location": st.column_config.TextColumn("Location"),
            "Rating": st.column_config.NumberColumn("Rating", format="%.1f ⭐"),
            "Price/Night": st.column_config.TextColumn("Price/Night"),
            "Total Cost": st.column_config.TextColumn(f"Total ({nights} nights)")
        }
    )

def extract_json_from_text(text):
    """Extract JSON array from text with improved robustness."""
    import re
    import json

    st.write(f"Attempting to extract JSON from: {text[:300]}...")

    json_pattern = r'\[.*?\]'
    matches = re.findall(json_pattern, text, re.DOTALL)
    
    if matches:
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue

    json_obj_pattern = r'\{.*?\}'
    obj_matches = re.findall(json_obj_pattern, text, re.DOTALL)
    
    if obj_matches:
        for match in obj_matches:
            try:
                result = json.loads(match)
                if isinstance(result, dict) and any(key in result for key in ['hotels', 'results', 'data']):
                    # Check if this object contains hotel data
                    for key in ['hotels', 'results', 'data']:
                        if key in result and isinstance(result[key], list):
                            return result[key]
                return [result] 
            except json.JSONDecodeError:
                continue
    
    return []

def display_welcome_screen():
    """Display welcome screen with instructions"""
    st.markdown("""
    <div class="status-box info-box">
        <h3>👋 Welcome to Hotel Finder!</h3>
        <p>Enter your travel details in the sidebar and click 'Search Hotels' to find the perfect accommodation for your trip.</p>
    </div>
    """, unsafe_allow_html=True)


    st.markdown('<h2 class="sub-header">Popular Destinations</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Mumbai</h3>
            <p>The city of dreams with world-class hotels</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Delhi</h3>
            <p>Experience the capital's luxury accommodations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>Goa</h3>
            <p>Beach resorts and boutique stays</p>
        </div>
        """, unsafe_allow_html=True)