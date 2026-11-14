from base import TestPlugin


class BatteryTest(TestPlugin):

    @property
    def name(self):
        return "cek_baterai"

    async def run(self, session):

        print("\n=== BATTERY TEST ===")

        result = await session.call_tool(self.name, {})

        for content in result.content:
            if content.type == "text":
                print(content.text)