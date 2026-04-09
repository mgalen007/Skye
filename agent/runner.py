from openai import OpenAI
from agent.dispatcher import dispatch
from tools import schemas as tools
import os, json
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def run_agent(messages: list[dict]) -> str:
    while True:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            tools=tools,
            messages=messages
        )

        choice = response.choices[0]

        # LLM calls no tools
        if choice.finish_reason == "stop":
            return choice.message.content
            break
        
        # LLM calls a tool
        if choice.finish_reason == "tool_calls":
            messages.append(choice.message)

            for tool_call in choice.message.tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                
                result = dispatch(
                    tool_name=name,
                    args=args
                )

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
