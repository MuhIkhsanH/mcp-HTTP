import subprocess

from core.plugin import Plugin


class BatteryPlugin(Plugin):

    def register_tools(self, mcp):

        @mcp.tool()
        def cek_baterai() -> str:
            """Melihat status, persentase, dan kondisi baterai laptop."""

            try:
                result = subprocess.run(
                    ["acpi"],
                    capture_output=True,
                    text=True,
                    check=True
                )

                return result.stdout.strip()

            except FileNotFoundError:
                return "Perintah acpi tidak ditemukan."

            except subprocess.CalledProcessError as error:
                return f"Gagal membaca baterai: {error.stderr.strip()}"