from catway import CatMail

def main():
    with CatMail("sadf@catway.org") as email:
        for mail in email.get_inboxes():
            print(mail)
            print(email.get_inbox(mail.id))

main()
