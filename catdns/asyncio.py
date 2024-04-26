from .async_session import process_request
from .types import FullMail

async def get_inbox(mail: str, timeout: int = 60, json: bool = False) -> "FullMail":
    result = await process_request(
        method="post",
        data={
            "mail": mail
        },
        timeout=timeout
    )

    if json:
        return result

    return FullMail.from_json(result)