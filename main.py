import streamlit as st
from datetime import timedelta
import json
import traceback

from config import GROQ_API_KEY, GRAPHHOPPER_API_KEY
from styles import STYLES
from utils.travel_utils import get_all_travel_distances, get_transport_icons
from utils.ui_utils import (
    display_travel_info, 
    display_hotel_results, 
    extract_json_from_text,
    display_welcome_screen
)
from agents.crew import setup_hotel_crew
from agents.hotel_agent import direct_hotel_search

st.set_page_config(
    page_title="Hotel Finder AI", 
    page_icon="🏨", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(STYLES, unsafe_allow_html=True)

if not GROQ_API_KEY or not GRAPHHOPPER_API_KEY:
    st.markdown("""
    <div class="status-box error-box">
        <h3>❌ API Keys Missing</h3>
        <p>Please set all required API keys before running the app.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

with st.sidebar:
    st.markdown("""
<div class="sidebar-header">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle; margin-right: 10px;">
        <path d="M7 13c1.66 0 3-1.34 3-3S8.66 7 7 7s-3 1.34-3 3 1.34 3 3 3zm12-6h-8v7H3V5H1v15h2v-3h18v3h2v-9c0-2.21-1.79-4-4-4z"/>
    </svg>
    Hotel Finder
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="sidebar-header">📍 Location</div>', unsafe_allow_html=True)
    state = st.text_input("State:", placeholder="e.g. Gujarat")
    city = st.text_input("City:", placeholder="e.g. Ahmedabad")
    user_city = st.text_input("Your Current City:", placeholder="Leave blank if same as destination")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-header">📅 Dates & Budget</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        check_in = st.date_input("Check-in:")
    with col2:
        check_out = st.date_input("Check-out:", value=check_in + timedelta(days=1))
    
    nights = (check_out - check_in).days
    if nights > 0:
        st.info(f"🌙 {nights} night{'s' if nights > 1 else ''}")
    
    budget = st.slider("Budget per night (₹):", min_value=500, max_value=10000, value=2000, step=500)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-header">🚆 Travel Mode</div>', unsafe_allow_html=True)
    travel_mode = st.radio(
        "Select your preferred mode of travel:",
        options=["road", "air", "railway"],
        format_func=lambda x: f"{get_transport_icons()[x]} {x.capitalize()}"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    search_button = st.button("🔍 Search Hotels", use_container_width=True)

if search_button:
    if not state or not city:
        st.warning("⚠️ Please enter both state and city to continue.")
    else:
        user_city = user_city.strip() or city
        
        try:
            direct_response = direct_hotel_search(city, state, budget)

            try:
                hotels = json.loads(direct_response)
            except json.JSONDecodeError:
                hotels = extract_json_from_text(direct_response)

            if isinstance(hotels, list) and len(hotels) > 0:
                if user_city.lower() != city.lower():
                    try:
                        distances = get_all_travel_distances(user_city, city)
                        if distances:
                            display_travel_info(user_city, city, travel_mode, distances)
                    except Exception as e:
                        st.warning(f"⚠️ Could not fetch travel info: {str(e)}")

                display_hotel_results(hotels, nights, check_in, check_out, travel_mode)
            else:
                st.error("❌ Could not extract valid hotel list from LLM output.")

        except Exception as e:
            st.markdown(f"""
            <div class="status-box error-box">
                <h3>❌ Application Error</h3>
                <p>An unexpected error occurred: {str(e)}</p>
            </div>
            """, unsafe_allow_html=True)
            with st.expander("Debug Information"):
                st.code(traceback.format_exc(), language="python")

else:
    display_welcome_screen()

st.markdown("""
<div style="margin-top: 2rem; text-align: center; padding: 1rem; border-top: 1px solid #f0f2f6;">
    <p>🏨 Hotel Finder AI | Powered by Groq & Graphhopper</p>
</div>
""", unsafe_allow_html=True)