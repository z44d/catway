from catdns import get_inbox

inbox = get_inbox("test1@catdns.in")

print(inbox.message)

for i in inbox.mail_data:
    print(i.sent_from)
    print(i.subject)