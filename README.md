# Install :
```commandline
pip install -U catdns
```

# How to use :
- 1 - Send email to your custom email, for example: ``test1@catdns.in``
- 2 - Get inbox:

```python
from catdns import get_inbox

inbox = get_inbox("test1@catdns.in")

print(inbox)
```