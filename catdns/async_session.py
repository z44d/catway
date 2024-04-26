import aiohttp
import ssl
import certifi

API_URL = "https://email.catdns.in/api"

class SessionManager:
    def __init__(self) -> None:
        self.session = None
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())


    async def create_session(self):
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(
            limit=50,
            ssl_context=self.ssl_context
        ))
        return self.session

    async def get_session(self):
        if self.session is None:
            self.session = await self.create_session()
            return self.session

        if self.session.closed:
            self.session = await self.create_session()

        # noinspection PyProtectedMember
        if not self.session._loop.is_running():
            await self.session.close()
            self.session = await self.create_session()
        return self.session


session_manager = SessionManager()

async def process_request(method: str, data: dict, timeout: int = 60, url: str = API_URL) -> dict:
    session = await session_manager.get_session()
    async with session.request(
        method=method,
        url=url,
        json=data,
        timeout=aiohttp.ClientTimeout(total=timeout),
    ) as response:
        return await response.json()
