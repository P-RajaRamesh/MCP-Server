# MCP Shell Server

A simple MCP (Model Context Protocol) server that provides a terminal tool for executing shell commands.

## Overview

This server exposes a single tool called `terminal` that allows executing terminal/shell commands and returns their output. It's built using the MCP Python SDK and enables LLM applications like Claude to run commands on your system.

## Installation

### Prerequisites

- Python 3.9+
- MCP Python SDK

### Setup

1. Install the MCP Python SDK and CLI:

```bash
pip install "mcp[cli]"
```

2. Clone this repository or download the server file.

## Usage

### Testing the Server

You can test the server using the MCP development tool:

```bash
mcp dev shellserver/server.py
```

This will start the server and open the MCP Inspector where you can test the terminal tool.

### Installing in Claude Desktop

To use the server with Claude Desktop:

```bash
mcp install shellserver/server.py
```

This will register the server with Claude Desktop, allowing you to use the terminal tool directly in Claude.

## Security Notice

⚠️ **CAUTION**: This server allows execution of any shell command. Use with caution as it can potentially:
- Modify or delete files
- Access sensitive information
- Run potentially harmful commands

Only use this server in trusted environments and be careful with the commands you approve for execution.

## Tool Reference

### terminal

Executes a shell command and returns its output.

**Parameters:**
- `command` (string): The command to execute

**Returns:**
- String: The command output (stdout and stderr combined)

**Example usage:**

```
terminal("ls -la")
terminal("echo Hello World")
terminal("pwd")
```

## License

[MIT License](LICENSE)
