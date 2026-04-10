from agent.runner import run_agent

while True:
    prompt = input("You -> ")
    messages = [
        { 
            "role": "system",
            "content": '''You are a friendly weather AI assistant
            When writing reports, make sure to extract meaningful data from the provided information,
            and make an easy to understand report in a human-readable format. Make sure to include ALL
            the weather data you get in the report, so that it is complete. One more thing, make sure 
            to write each weather attribute on a different line so it is visually appealing.'''
        
        },
        { "role": "user", "content": prompt }
    ]
    result = run_agent(messages)
    print(f"Model -> {result}")