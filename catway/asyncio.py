from .async_session import process_request, session_manager
from .types import Mail, MailBox
from .utils import ApiExeption

from typing import AsyncGenerator, Any

class CatMail:
    def __init__(self, email: str) -> None:
        """
        Args:
            email (str): the email, example : test@catway.org
        """
        self.email = email
        self.username = email.split("@")[0]

    async def get_inboxes(self, limit: int = None, timeout: int = 60) -> AsyncGenerator["Mail", Any]:
        request_url = "https://mail.catway.org/api/{username}/email".format(username=self.username)
        result = await process_request(url=request_url, timeout=timeout)
        if not result["ok"]:
            raise ApiExeption(result["error"])

        count = 0

        for i in result["data"]["mails"]:
            if limit is not None and count == limit:
                return
            count += 1
            yield Mail.from_json(i)

    async def get_inbox(self, id: str, timeout: int = None) -> "MailBox":
        request_url = "https://mail.catway.org/api/{id}/inbox".format(id=id)
        result = await process_request(url=request_url, timeout=timeout)
        if not result["ok"]:
            raise ApiExeption(result["error"])
        return MailBox.from_json(result["data"])

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        session = await session_manager.get_session()
        return await session.close()