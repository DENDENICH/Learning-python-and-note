import asyncio
from aiohttp import ClientSession, BasicAuth


proxy = "http://ip:port"
proxy_auth = BasicAuth(login="login", password="password")

api_key = "xxx"

base_url = "https://example.com"
data_query = {"query": "man"}
headers = {
	"Authorization:": f"Bearer {api_key}",
}


async def get_query():
    async with ClientSession(proxy=proxy, proxy_auth=proxy_auth, headers=headers) as session:
        async with session.get(url=base_url, params=data_query) as response:
            print(response.status)
            print(await response.json())


if __name__ == "__main__":
    asyncio.run(get_query())
