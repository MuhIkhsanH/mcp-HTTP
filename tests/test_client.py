import asyncio
import subprocess
import importlib
import inspect
import pkgutil
import os

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

from base import TestPlugin


def load_plugins():

    plugins = []

    for module in pkgutil.iter_modules([os.path.dirname(__file__)]):
        if module.name in ("base", "test_client"):
            continue

        imported = importlib.import_module(module.name)

        for _, cls in inspect.getmembers(imported, inspect.isclass):
            if issubclass(cls, TestPlugin) and cls is not TestPlugin:
                plugins.append(cls())

    return plugins


async def main():

    url = "http://localhost:8000/mcp"
    plugins = load_plugins()

    async with streamablehttp_client(url) as (read, write, _):
        async with ClientSession(read, write) as session:

            await session.initialize()

            print("\n=== CONNECTED ===")

            result = await session.list_tools()

            print("\n=== AVAILABLE TOOLS ===")

            for tool in result.tools:
                print(f"- {tool.name}: {tool.description}")

            selected = subprocess.run(
                [
                    "fzf",
                    "--prompt=Jalankan fitur > ",
                    "--header=ESC untuk keluar"
                ],
                input="\n".join(plugin.name for plugin in plugins),
                stdout=subprocess.PIPE,
                stderr=None,
                text=True
            )

            if selected.returncode == 0:
                name = selected.stdout.strip()

                for plugin in plugins:
                    if plugin.name == name:
                        await plugin.run(session)
                        break


if __name__ == "__main__":
    asyncio.run(main())