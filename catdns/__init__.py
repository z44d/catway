__version__ = "2.1"

from .session import make_request
from .types import Mail, MailBox
from .utils import ApiExeption

from typing import List

class CatMail:
    def __init__(self, email: str) -> None:
        """
        Args:
            email (str): the email, example : test@catway.org
        """
        self.email = email
        self.username = email.split("@")[0]

    def get_inboxes(self, limit: int = None, timeout: int = 60) -> List["Mail"]:
        request_url = "https://mail.catway.org/api/{username}/email".format(username=self.username)
        result = make_request(url=request_url, timeout=timeout)
        if not result["ok"]:
            raise ApiExeption(result["error"])

        _ = []
        for i in result["data"]["mails"]:
            if limit is not None and len(_) == limit:
                break
            _.append(Mail.from_json(i))

        return _

    def get_inbox(self, id: str, timeout: int = None) -> "MailBox":
        request_url = "https://mail.catway.org/api/{id}/inbox".format(id=id)
        result = make_request(url=request_url, timeout=timeout)
        if not result["ok"]:
            raise ApiExeption(result["error"])
        return MailBox.from_json(result["data"])

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self