
import subprocess
import webbrowser

from core.plugin import Plugin


class YouTubePlugin(Plugin):

    def register_tools(self, mcp):

        @mcp.tool()
        def search_youtube(query: str) -> str:
            """
            Mencari video YouTube berdasarkan kata kunci.
            Mengembalikan judul dan ID video.
            """

            try:
                result = subprocess.run(
                    [
                        "yt-dlp",
                        "--flat-playlist",
                        "--dump-json",
                        "--playlist-end", "5",
                        f"ytsearch5:{query}"
                    ],
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                if result.returncode != 0:
                    return f"Gagal mencari video: {result.stderr}"

                import json

                videos = []

                for line in result.stdout.splitlines():
                    data = json.loads(line)

                    videos.append(
                        f"Judul: {data.get('title')}\n"
                        f"ID: {data.get('id')}\n"
                    )

                if not videos:
                    return "Video tidak ditemukan."

                return "\n".join(
                    f"{i + 1}. {video}"
                    for i, video in enumerate(videos)
                )

            except Exception as e:
                return f"Error: {e}"

        @mcp.tool()
        def play_youtube(video_id: str) -> str:
            """
            Membuka dan memutar video YouTube berdasarkan ID.
            """

            url = f"https://www.youtube.com/watch?v={video_id}"

            if webbrowser.open(url):
                return f"Video berhasil dibuka: {url}"

            return "Gagal membuka browser."
