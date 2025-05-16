# MCP Shell Server

A simple MCP (Model Context Protocol) server that provides a terminal tool for executing shell commands.

## Overview

This server exposes a single tool called `terminal` that allows executing terminal/shell commands and returns their output. It's built using the MCP Python SDK and enables LLM applications like Claude to run commands on your system.

## Installation

### Prerequisites

- Python 3.9+
- MCP Python SDK

### Setup
1. Create virtual environment
 ```bash
uv venv
```
2. Activate it:
```bash
.venv\Scripts\activate
```
3. Install the MCP Python SDK and CLI:
```bash
uv add "mcp[cli]"
```
4. Clone this repository or download the server file.
5. To build docker image:
```bash
docker build -t shellserver-app .
```
6. To run docker image: 
```bash
docker run -it --rm shellserver-app
```

### Useful commands:
- list docker image: 
```bash
docker image ls
```
- list docker running: 
```bash
docker ps
```
- To kill docker:
```bash
docker kill docker_id
```
- To interact with docker container ():
```bash
docker exec -it docker_id sh
```

### Installing in Claude Desktop

To use the server with Claude Desktop upadte the Claude config file:

```bash
{
  "mcpServers": {
	"docker-shell": {
		"command": "docker",
		"args": [ "run", "-i", "--rm", "--init", "-e", "DOCKER_CONTAINER=true", "shellserver-app" ]
	}
  }
}
```

This will register the server with Claude Desktop, allowing you to use the terminal tool directly in Claude.

## Security Notice

⚠️ **CAUTION**: This server allows execution of any shell command. Use with caution as it can potentially:
- Modify or delete files
- Access sensitive information
- Run potentially harmful commands

Only use this server in trusted environments and be careful with the commands you approve for execution.

## License

[MIT License](LICENSE)
