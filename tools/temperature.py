import subprocess

from core.plugin import Plugin


class TemperaturePlugin(Plugin):

    def register_tools(self, mcp):

        @mcp.tool()
        def cek_suhu() -> str:
            """Melihat suhu CPU dan setiap core prosesor laptop."""

            try:
                result = subprocess.run(
                    ["sensors", "coretemp-isa-0000"],
                    capture_output=True,
                    text=True,
                    check=True
                )

                return result.stdout.strip()

            except FileNotFoundError:
                return "Perintah sensors tidak ditemukan."

            except subprocess.CalledProcessError as error:
                return f"Gagal membaca suhu: {error.stderr.strip()}"