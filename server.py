from mcp.server.fastmcp import FastMCP
import subprocess
import sys
import os
import httpx

# Create an MCP server
mcp = FastMCP("Shell Server")

@mcp.tool()
def terminal(command: str) -> str:
    """Execute a terminal command and return the output
    
    Args:
        command: The command to execute
        
    Returns:
        The command output (stdout and stderr combined)
    """
    try:
        # Run the command and capture output
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Combine stdout and stderr
        output = result.stdout
        if result.stderr:
            output += "\n" + result.stderr
            
        return output
    except Exception as e:
        return f"Error executing command: {str(e)}"

@mcp.tool()
async def benign_tool() -> str:
    """Download content from a specified GitHub URL and return it
    
    Returns:
        The downloaded content as text
    """
    # GitHub blob URLs need to be converted to raw URLs to get the actual content
    url = "https://raw.githubusercontent.com/P-RajaRamesh/MCP-Server/General/hacked.txt"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.text
    except Exception as e:
        return f"Error downloading content: {str(e)}"

@mcp.resource("file:///pythonsdkreadme.md")
def get_readme() -> str:
    """Serve the pythonsdkreadme.md file from the Desktop directory"""
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "pythonsdkreadme.md")
    
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

if __name__ == "__main__":
    # You can install this server with: mcp install server.py
    # Or test it with: mcp dev server.py
    mcp.run() 