from json import dumps
from typing import List, Dict

class Parser:
    def __init__(self):
        pass

    @staticmethod
    def default(obj: "Parser"):
        if isinstance(obj, bytes):
            return repr(obj)

        return {
            **{
                attr: (
                    getattr(obj, attr)
                )
                for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
                if getattr(obj, attr) is not None
            }
        }

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Parser.default, ensure_ascii=False)

    def __eq__(self, other: "Parser") -> bool:
        for attr in self.__dict__:
            try:
                if attr.startswith("_"):
                    continue

                if getattr(self, attr) != getattr(other, attr):
                    return False
            except AttributeError:
                return False

        return True

    def __repr__(self) -> str:
        return "".format(
            self.__class__.__name__,
            ", ".join(
                f"{attr}={repr(getattr(self, attr))}"
                for attr in filter(lambda x: not x.startswith("_"), self.__dict__)
                if getattr(self, attr) is not None
            )
        )

    def __setstate__(self, state):
        self.__dict__ = state

    def __getstate__(self):
        state = self.__dict__.copy()

        return state

class MailData(Parser):
    def __init__(
            self,
            content: str = None,
            type: str = None,
            html: str = None
        ):
            self.content = content
            self.type = type
            self.html = html

    @staticmethod
    def from_json(_d: Dict) -> "MailData":
        return MailData(
            content=_d.get("content"),
            type=_d.get("type"),
            html=_d.get("textAsHtml")
        )

class Mail(Parser):
    def __init__(
        self,
        data: "MailData" = None,
        date: str = None,
        sent_from: "MailFrom" = None,
        subject: str = None
    ):
        self.data = data
        self.date = date
        self.sent_from = sent_from
        self.subject = subject

    @staticmethod
    def from_json(_d: Dict) -> "Mail":
        return Mail(
            data=MailData.from_json(_d.get("data")),
            date=_d.get("date"),
            sent_from=MailFrom.from_json(_d.get("sentFrom")),
            subject=_d.get("subject")
        )

class MailFrom(Parser):
    def __init__(
        self,
        email: str = None,
        user: str = None
    ):
        self.email = email
        self.user = user

    @staticmethod
    def from_json(_d: Dict) -> "MailFrom":
        return MailFrom(
            email=_d.get("email"),
            user=_d.get("user")
        )

class FullMail(Parser):
    def __init__(
            self,
            mail_data: List["Mail"] = None,
            message: str = None
        ):
            self.mail_data = mail_data
            self.message = message

    @staticmethod
    def from_json(_d: Dict) -> "FullMail":
        return FullMail(
            mail_data=[Mail.from_json(i) for i in _d.get("mailData")] if _d.get("mailData") else None,
            message=_d.get("message")
        )