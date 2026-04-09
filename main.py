from agent.runner import run_agent

while True:
    prompt = input("You -> ")
    messages = [
        { "role": "user", "content": prompt },
        { 
            "role": "system",
            "content": '''You are a friendly AI assistant, sometimes when you call tools, you may not get a valid or expected output
            make sure that you handle it gracefully, and explain the problem.'''
        
        }
    ]
    result = run_agent(messages)
    print(f"Model -> {result}")