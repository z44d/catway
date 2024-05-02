from datetime import datetime
from typing import Union

__all__ = [
    "str_to_datetime",
    "convert_to_datetime",
    "convert_to_str",
    "ApiExeption"
]

class ApiExeption(Exception):
    pass

def str_to_datetime(_s: str) -> "datetime":
    return datetime.strptime(_s, "%Y-%m-%dT%H:%M:%S.%fZ")

def convert_to_datetime(_s: str = None) -> Union["datetime", "None"]:
    if _s is not None:
        return str_to_datetime(_s)
    else:
        return None

def convert_to_str(_d: datetime = None) -> "str":
    if _d is not None:
        return str(_d)
    else:
        return None