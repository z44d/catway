# Install :
```commandline
pip install -U catdns
```

# How to use :
- 1 - Send email to your custom email, for example: ``sadf@catway.org``
- 2 - Get inbox:

```python
from catdns import CatMail

def main():
    with CatMail("sadf@catway.org") as email:
        for mail in email.get_inboxes():
            print(mail)
            print(email.get_inbox(mail.id))

main()
```