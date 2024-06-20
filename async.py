import aiohttp
import asyncio

async def main():
    
    websites = {"google": "https://google.com/",
                "yandex": "https://yandex.com/",
                "amazon": "https://amazon.com/",
                "bad website": "https://badweb.site/"}

    async with aiohttp.ClientSession() as session:
        for website in websites.items():
            url = website[1]
            try:
                async with session.get(url) as resp:
                    status = resp.status
                    if status < 400 or status >= 500:
                        print(f"{website[0]} is available")
                    else:
                        print(f"{website[0]} is not available")
            except:
                print(f"{website[0]} is not available")

asyncio.run(main())