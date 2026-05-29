from fastmcp import FastMCP
import json
from pathlib import Path
from typing import Any
import requests
from typing import List, Dict

mcp = FastMCP("Fun-MCP Server")

# Load person data from JSON file once at server start

# Define person_data at module level to be accessible by tool functions
person_file = Path(__file__).parent / "data" / "persons.json"
with open(person_file, "r") as f:
    person_data = json.load(f)

@mcp.tool(name="person-info", description="Default - Find information about Arun")
def find_person() -> dict:
    # Use the module-level variable here
    return person_data


@mcp.tool(name="blog-search", description="Search blog - search Arun's Blog")
def search_blog(queryStr: str) -> List[Dict[str, str]]:
    try:
        url = "http://localhost:9000/search"
        params = {"query": queryStr}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises HTTPError if status is 4xx, 5xx
        result = response.json()  # Expecting a JSON array of objects (list of dicts)
        if isinstance(result, list):
            return result
        else:
            return []  # Return empty list if result isn't a list
    except Exception as e:
        print(f"Error during blog search: {e}")
        return []  

if __name__ == "__main__":
    # mcp.run(transport="streamable-http", port=8001)
    mcp.run(transport="stdio")