from agent.runner import run_agent

# ANSI escape codes for colors and styles
BOLD = '\033[1m'
RESET = '\033[0m'
GREEN = '\033[32m'
BLUE = '\033[34m'
CYAN = '\033[36m'
YELLOW = '\033[33m'

print(f"""
{BOLD}{CYAN}╔══════════════════════════════╗
║          SKYE v1.0           ║
╚══════════════════════════════╝{RESET}
""")

while True:
    prompt = input(f"{GREEN}You: {RESET}")
    print()  # Add a line break after input
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
    print(f"{BLUE}SKYE:{RESET} {result}")
    print(f"{YELLOW}─" * 40 + f"{RESET}")  # Separator line