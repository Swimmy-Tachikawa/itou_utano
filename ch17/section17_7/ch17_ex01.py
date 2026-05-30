import asyncio

class Downloader:
    async def download(self, file, sec):
        await asyncio.sleep(sec)
        print(f"{file} のダウンロード完了")

d = Downloader()
t1 = asyncio.create_task(d.download("movie.mp4", 3))
t2 = asyncio.create_task(d.download("music.mp3", 2))
t3 = asyncio.create_task(d.download("doc.pdf", 1))

