# MCP Client-Server Sentiment Analysis

This project exposes the sentiment analysis tool from mcp_server.py and that tool will be consumed in any client application like claude or any custom client application like mcp_client.py

## 🚀 Features
- *Sentiment Analysis*: Using TextBlob to analyze text polarity and subjectivity.
- *MCP-Enabled AI Agent*: Allows tool integration via MCP protocol with remote execution.
- *Gradio UI*: Interactive user interface for real-time sentiment analysis and agent-based queries.
- *Efficient Dependency Management*: Uses uv for optimal package handling.

## 🛠 Installation

Ensure you have *uv* installed. If not, install it first:
uv will be installed in my conda virtual environment
```
pip install uv
```

Now create a virtual environment:
```
uv venv
```

Activate the virtual environment:
```
.venv\Scripts\activate
```

Now, initialize uv project and install dependencies:
```
uv init
```
```
uv add -r requirements.txt
```

## 🔥 Running the Project

Start the **MCP Server**:
```
python mcp_server.py
```
Using this tools in **Claude Desktop** by editing **claude_desktop_config.json** file:
```
{
  "mcpServers": {
    "gradio": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://localhost:7860/gradio_api/mcp/sse"
      ]
    }
  }
}
```

USing this tool in client application - Launch the **MCP Client**:
```
python mcp_client.py
```

## 🌐 Deploy mcp_server in Huggingface
- Make sure change the mcp_server.py to app.py
- Select the Gradio app in Huggingface Spaces
- Login to huggingface from command prompt using ```huggingface-cli login```.
- Enter the access huggingface access token and follow the below commands to push to huggingface spaces.
```
git init
git add app.py requirements.txt
git commit -m "Initial commit"
git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/mcp-sentiment
git push origin master:main --force
```

Using this remote tool in **Claude Desktop** by editing **claude_desktop_config.json** file:
```
{
  "mcpServers": {
    "gradio": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://user_name-mcp-sentiment.hf.space/gradio_api/mcp/sse"
      ]
    }
  }
}
```
