import gradio as gr

import os

from smolagents import InferenceClientModel, CodeAgent#, ToolCollection
from smolagents.mcp_client import MCPClient


try:
    mcp_client = MCPClient(
        ## Try this working example on the hub:
        # {"url": "https://abidlabs-mcp-tools.hf.space/gradio_api/mcp/sse"} # --server: https://huggingface.co/spaces/abidlabs/mcp-tools
        {"url": "https://rajaramesh-mcp-sentiment.hf.space/gradio_api/mcp/sse",
         "transport": "sse" # You can change to "streamable-http" when updating to version 1.20
         } # --remote server: https://huggingface.co/spaces/rajaramesh/mcp-sentiment/
        # {"url": "http://localhost:7860/gradio_api/mcp/sse"} # --local server
    )
    tools = mcp_client.get_tools()
    print(f"my tools: {[*tools]}")

    model = InferenceClientModel(
        model_id="deepseek-ai/DeepSeek-R1",
        provider="together",
        token=os.getenv('HF_TOKEN')
    )
    
    agent = CodeAgent(tools=[*tools], model=model)

    demo = gr.ChatInterface(
        fn=lambda message, history: str(agent.run(message)), #here chat interface will run the function and provides 2 arguments
        type="messages",
        examples=["Prime factorization of 68"],
        title="Agent with MCP Tools",
        description="This is a simple agent that uses MCP tools to answer questions.",
    )

    demo.launch()
finally:
    mcp_client.disconnect()