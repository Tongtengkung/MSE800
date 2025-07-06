from together import Together

# Replace this with your actual Together API key
TOGETHER_API_KEY = "enter your own key please"

client = Together(api_key=TOGETHER_API_KEY)

def instructor_chatbot():
    """Command-line AI Itinerary Chatbot."""
    print("Welcome to AI Itinerary Recommender!")
    print("Answer a few questions to get a personalized travel plan.\n")

    try:
        # Collect user input
        days = input("How many days will you travel? ")
        location = input("Where are you going (city)? ")
        age_range = input("What's your age range (e.g., 18-35)? ")
        number_of_people = input("How many people are traveling? ")
        group_type = input("What group type? (e.g., family, solo, friends) ")
        activity_level = input("Preferred activity level? (low, medium, high) ")
        budget = input("Budget? (low, medium, high) ")
        season = input("Which season? (e.g., summer, winter) ")
        accommodation = input("Accommodation preference? (hotel, Airbnb, hostel) ")
        transportation = input("Transportation preference? (public, rental car) ")
        pace = input("Preferred travel pace? (relaxed, moderate, fast) ")
        any_comments = input("Any additional comments or preferences? ")

        # Build prompt
        prompt = f"""
You are a professional tourist itinerary planner. Recommend a structured itinerary based on the following details:

- Duration: {days} days
- Destination: {location}
- Age Range: {age_range}
- Group Size: {number_of_people}
- Group Type: {group_type}
- Activity Level: {activity_level}
- Budget: {budget}
- Season: {season}
- Accommodation Type: {accommodation}
- Transportation: {transportation}
- Travel Pace: {pace}
- Additional Comments: {any_comments}

Please provide a day-by-day travel itinerary with up to 3 activities per day. Each activity should include:
- Name
- Address (if available)
- Short description
"""

        # Send to Together API using a serverless-supported model
        response = client.chat.completions.create(
            model="meta-llama/Llama-3-70b-chat-hf",  # ✅ Serverless model
            messages=[
                {"role": "system", "content": "You are a helpful itinerary planner."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )

        # Print the itinerary
        print("\nHere's your personalized itinerary:\n")
        print(response.choices[0].message.content.strip())
        print("\nThank you for using Hadi, your AI travel planner! ✈️")

    except Exception as e:
        print("Error during itinerary generation:", e)

# Run the chatbot
if __name__ == "__main__":
    instructor_chatbot()
