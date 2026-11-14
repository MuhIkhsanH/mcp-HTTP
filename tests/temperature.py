from base import TestPlugin


class TemperatureTest(TestPlugin):

    @property
    def name(self):
        return "cek_suhu"

    async def run(self, session):

        print("\n=== CPU TEMPERATURE TEST ===")

        result = await session.call_tool(self.name, {})

        for content in result.content:
            if content.type == "text":
                print(content.text)