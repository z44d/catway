from pydantic import BaseModel
from datetime import datetime
from typing_extensions import TypedDict

from .utils import convert_to_datetime, convert_to_str

class Object(BaseModel):
    def __str__(self: "Object"):
        return self.model_dump_json(indent=4)

class MailDict(TypedDict):
    id: "str"
    senderEmail: "str"
    senderName: "str"
    subject: "str"
    createdAt: "str"
    updatedAt: "str"
    expireAt: "str"

class Mail(Object):
    id: str
    sender_email: "str"
    sender_name: "str"
    subject: "str"
    created_at: "datetime"
    updated_at: "datetime"
    expire_at: "datetime"

    @staticmethod
    def from_json(_d: "MailDict") -> "Mail":
        to_parse = {
            "id": _d.get("id"),
            "sender_email": _d.get("senderEmail"),
            "sender_name": _d.get("senderName"),
            "subject": _d.get("subject"),
            "created_at": convert_to_datetime(_d.get("createdAt")),
            "updated_at": convert_to_datetime(_d.get("updatedAt")),
            "expire_at": convert_to_datetime(_d.get("expireAt"))
        }
        return Mail(**to_parse)

    @property
    def view_link(self) -> "str":
        return "https://mail.catway.org/inbox/{id}".format(id=self.id)

    @property
    def raw(self) -> "MailDict":
        return {
            "id": self.id,
            "senderEmail": self.sender_email,
            "senderName": self.sender_name,
            "subject": self.subject,
            "createdAt": convert_to_str(self.created_at),
            "updatedAt": convert_to_str(self.updated_at),
            "expireAt": convert_to_str(self.expire_at)
        }

class MailBoxDict(TypedDict):
    id: str
    html: str
    content: str
    senderEmail: "str"
    senderName: "str"
    subject: "str"
    createdAt: "str"
    updatedAt: "str"
    expireAt: "str"
    mailboxOwner: "str"

class MailBox(Object):
    id: "str"
    html: "str"
    content: "str"
    sender_email: "str"
    sender_name: "str"
    subject: "str"
    created_at: "datetime"
    updated_at: "datetime"
    expire_at: "datetime"
    owner: "str"

    @staticmethod
    def from_json(_d: "MailBoxDict") -> "MailBox":
        to_parse = {
            "id": _d.get("id"),
            "html": _d.get("html"),
            "content": _d.get("content"),
            "sender_email": _d.get("senderEmail"),
            "sender_name": _d.get("senderName"),
            "subject": _d.get("subject"),
            "created_at": convert_to_datetime(_d.get("createdAt")),
            "updated_at": convert_to_datetime(_d.get("updatedAt")),
            "expire_at": convert_to_datetime(_d.get("expireAt")),
            "owner": _d.get("mailboxOwner"),
        }
        return MailBox(**to_parse)

    @property
    def view_link(self) -> "str":
        return "https://mail.catway.org/inbox/{id}".format(id=self.id)

    @property
    def raw(self) -> "MailBoxDict":
        return {
            "id": self.id,
            "html": self.html,
            "content": self.content,
            "senderEmail": self.sender_email,
            "senderName": self.sender_name,
            "subject": self.subject,
            "createdAt": convert_to_str(self.created_at),
            "updatedAt": convert_to_str(self.updated_at),
            "expireAt": convert_to_str(self.expire_at),
            "mailboxOwner": self.owner
        }