import asyncio
from catdns.asyncio import CatMail

async def main():
    async with CatMail("sadf@catway.org") as email:
        async for mail in email.get_inboxes():
            print(mail)
            print(await email.get_inbox(mail.id))

asyncio.run(main())