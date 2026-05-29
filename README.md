## MCP Server
Fun MCP Starter project

## Python version requirement
python>=3.10



## setup local environment

python3.13 -m venv myenv
source myenv/bin/activate
pip install -U pip setuptools wheel
pip install -r requirements.txt


# Test Run
uv run server.py

make sure there are no errors and exit ,we will call this from claude

# claude config

```
"mcpServers": {
    "fun-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/project-folder/fun-mcp",
        "run",
        "server.py"
      ],
      "env": {}
    }
  },
 ```


 # debugging

 if needed tail logs to see logs and fix if required

 ```
 tail -n 20 -F ~/Library/Logs/Claude/mcp*.log
 ```
