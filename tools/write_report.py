
write_report_schema = {
    "type": "function",
    "function": {
        "name": "write_report",
        "description": "Write report to a specified filename, use this when the user tells you to write a report",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "The file to write the report to, it should be in the format of report_filename.txt unless specified otherwise."
                },
                "content": {
                    "type": "string",
                    "description": "This is the actual contents of the report, it should contain the weather description and the city name"
                }
            },
            "required": ["filename", "content"]
        }
    }
}

def write_report(filename: str, content: str) -> str:
    with open(filename, "w") as f:
        f.write(content)
    return f"Wrote report to {filename}"