from agent.runner import run_agent

while True:
    prompt = input("You: ")
    messages = [{"role": "user", "content": prompt}]
    result = run_agent(messages)
    print(f"(model): {result}") 