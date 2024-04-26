__version__ = "1.0.0"

from .session import make_request
from .types import FullMail

def get_inbox(mail: str, timeout: int = 60, json: bool = False) -> "FullMail":
    result = make_request(
        method="post",
        data={
            "mail": mail
        },
        timeout=timeout
    )

    if json:
        return result

    return FullMail.from_json(result)