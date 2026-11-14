from mcp.server.fastmcp import FastMCP

from core.loader import load_plugins


mcp = FastMCP(
    name="mcpHTTP",
    host="0.0.0.0",
    port=8000
)


def register_plugins():
    plugins = load_plugins()

    for plugin in plugins:
        plugin.register_tools(mcp)
        print(f"[PLUGIN] {plugin.__class__.__name__} loaded")


if __name__ == "__main__":
    register_plugins()

    print("[SERVER] mcpHTTP starting...")
    print("[SERVER] Endpoint: http://localhost:8000/mcp")

    mcp.run(transport="streamable-http")