
import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():

     url = "http://localhost:8000/mcp"
    

    async with streamablehttp_client(url) as (read, write, _):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print("\n=== CONNECTED ===")

            result = await session.list_tools()

            print("\n=== AVAILABLE TOOLS ===")

            for tool in result.tools:
                print(f"- {tool.name}: {tool.description}")

            print("\n=== BATTERY TEST ===")

            battery = await session.call_tool(
                "cek_baterai",
                {}
            )

            for content in battery.content:
                if content.type == "text":
                    print(content.text)

            print("\n=== CPU TEMPERATURE TEST ===")

            temperature = await session.call_tool(
                "cek_suhu",
                {}
            )

            for content in temperature.content:
                if content.type == "text":
                    print(content.text)


if __name__ == "__main__":
    asyncio.run(main())
