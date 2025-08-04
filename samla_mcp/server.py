from fastmcp import FastMCP

mcp = FastMCP(name="samla-mcp", version="0.1.0")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

"""
Publicly exposed function to run the server
"""
def run_server():
    mcp.run(transport="stdio")