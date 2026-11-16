
import subprocess
from core.plugin import Plugin


class VolumePlugin(Plugin):

    def register_tools(self, mcp):

        @mcp.tool()
        def atur_volume(volume: int) -> str:
            """
            Mengatur volume laptop dari 0 sampai 100 persen.
            """

            if not 0 <= volume <= 100:
                return "Volume harus antara 0 sampai 100."

            try:
                subprocess.run(
                    [
                        "pactl",
                        "set-sink-volume",
                        "@DEFAULT_SINK@",
                        f"{volume}%"
                    ],
                    check=True
                )

                return f"Volume berhasil diatur ke {volume}%."

            except FileNotFoundError:
                return "Perintah pactl tidak ditemukan."

            except subprocess.CalledProcessError:
                return "Gagal mengatur volume."
