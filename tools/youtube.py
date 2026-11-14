import webbrowser
from urllib.parse import quote_plus

from core.plugin import Plugin


class YouTubePlugin(Plugin):

    def register_tools(self, mcp):

        @mcp.tool()
        def buka_youtube(query: str = "") -> str:
            """
            Membuka YouTube dan mencari video berdasarkan permintaan pengguna.
            AI harus menentukan query pencarian berdasarkan konteks percakapan.
            Jika query kosong, buka halaman utama YouTube.
            """

            if query:
                url = (
                    "https://www.youtube.com/results?search_query="
                    + quote_plus(query)
                )
            else:
                url = "https://www.youtube.com"

            success = webbrowser.open(url)

            if success:
                return f"YouTube berhasil dibuka. Pencarian: {query or 'Halaman utama'}"

            return "Gagal membuka browser."