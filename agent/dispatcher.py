from tools import tools

def dispatch(tool_name: str, args: dict) -> str:
    tool = tools.get(tool_name)
    print(f"Using tool: {tool_name}")
    if not tool:
        return f"Error: Unknown tool {tool_name}"
    return tool(**args)