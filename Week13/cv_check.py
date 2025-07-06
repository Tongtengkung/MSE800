from together import Together

# Replace this with your actual Together API key
TOGETHER_API_KEY = "340d5d104893bda9d7930206eb4e597134c81d1df76e3aedb192acdc06426466"

client = Together(api_key=TOGETHER_API_KEY)

def instructor_chatbot():
    """Command-line AI CV comment."""
    print("Welcome to AI Comment on your CV!")
    print("Answer a few questions to get a your target for your CV.\n")

    try: