from crewai import Crew
from agents.hotel_agent import (
    get_llm, 
    create_hotel_agent, 
    create_distance_agent,
    create_hotel_task,
    create_distance_task
)

def setup_hotel_crew(city, state, user_city, budget, check_in, check_out, travel_mode):
    """Set up and return the CrewAI for hotel search"""
    llm = get_llm()

    hotel_finder = create_hotel_agent(llm)
    distance_estimator = create_distance_agent(llm)

    fetch_hotels_task = create_hotel_task(hotel_finder, city, state, budget, check_in, check_out)
    route_task = create_distance_task(distance_estimator, user_city, city, travel_mode)

    tasks = [fetch_hotels_task]

    return Crew(
        agents=[hotel_finder, distance_estimator],
        tasks=tasks,
        verbose=True
    )