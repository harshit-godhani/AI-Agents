from crewai import Agent
from langchain_groq import ChatGroq
from config import GROQ_API_KEY

def direct_hotel_search(city, state, budget):
    """Search for hotels directly using the LLM without CrewAI"""
    llm = ChatGroq(
        model="llama3-70b-8192",
        temperature=0.2,
        api_key=GROQ_API_KEY
    )
    
    prompt = f"""
    Find 5 hotels in {city}, {state}, India within a budget of ₹{budget} per night.
    
    For each hotel provide:
    1. Hotel name
    2. Price per night in rupees (within budget)
    3. Rating (out of 5)
    4. Location (area in {city})
    
    IMPORTANT: Return ONLY a JSON array with no explanations or additional text.
    The response should look exactly like this example:
    [
        {{"name": "Hotel Taj", "price": 1800, "rating": 4.2, "location": "MG Road"}},
        {{"name": "Grand Plaza", "price": 1600, "rating": 3.8, "location": "Park Street"}}
    ]
    """
    
    response = llm.invoke(prompt)
    return response.content
def create_hotel_agent(llm):
    """Create and return a hotel finder agent"""
    return Agent(
        role="Hotel Finder",
        goal="Find budget-friendly hotels in Indian cities.",
        backstory="An AI travel assistant specializing in hotel searches.",
        verbose=True,
        llm=llm
    )

def create_distance_agent(llm):
    """Create and return a distance estimator agent"""
    return Agent(
        role="Distance Estimator",
        goal="Estimate travel distances between cities.",
        backstory="Uses Graphhopper API for real-time distances.",
        verbose=True,
        llm=llm
    )

def get_llm():
    """Create and return the LLM instance"""
    return ChatGroq(
        model="groq/llama3-70b-8192",
        temperature=0.2,
        api_key=GROQ_API_KEY
    )

def create_hotel_task(hotel_agent, city, state, budget, check_in, check_out):
    """Create a task for finding hotels"""
    from crewai import Task
    
    hotel_description = f"""
    Find 6 hotels in {city}, {state} within a budget of ₹{budget} per night.
    Check-in date: {check_in.strftime("%Y-%m-%d")}
    Check-out date: {check_out.strftime("%Y-%m-%d")}
        
    For each hotel provide:
    1. Hotel name
    2. Price per night in rupees (within budget)
    3. Rating (out of 5)
    4. Location
    
    Format the results as a JSON array of objects with 'name', 'price', 'rating', and 'location' keys.
    You must return ONLY the JSON array with no additional explanations.
    
    Example output:
    [
        {{"name": "Hotel Taj", "price": 1800, "rating": 4.2, "location": "MG Road"}},
        {{"name": "Grand Plaza", "price": 1600, "rating": 3.8, "location": "Park Street"}}
    ]
    """

    return Task(
        description=hotel_description,
        expected_output="A JSON list of hotels with name, price, rating, and location.",
        agent=hotel_agent
    )

def create_distance_task(distance_agent, user_city, city, travel_mode):
    """Create a task for estimating distances"""
    from crewai import Task
    
    distance_description = f"Fetch the travel distance between {user_city} and {city} via {travel_mode}."
    
    return Task(
        description=distance_description,
        expected_output="Real-time travel distance between two cities.",
        agent=distance_agent
    )