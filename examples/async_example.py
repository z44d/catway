from catdns.asyncio import get_inbox

async def main():
    inbox = await get_inbox("test1@catdns.in")

    print(inbox.message)

    for i in inbox.mail_data:
        print(i.sent_from)
        print(i.subject)

import asyncio
asyncio.get_event_loop().run_until_complete(main())