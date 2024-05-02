import requests
import threading
from datetime import datetime

thread_local = threading.local()
SESSION_TIME_TO_LIVE = 600

session = None


def per_thread(key, construct_value, reset=False):
    """
    :meta private:
    """
    if reset or not hasattr(thread_local, key):
        value = construct_value()
        setattr(thread_local, key, value)

    return getattr(thread_local, key)

def _get_req_session(reset=False):
    if SESSION_TIME_TO_LIVE:
        # If session TTL is set - check time passed
        creation_date = per_thread('req_session_time', lambda: datetime.now(), reset)
        # noinspection PyTypeChecker
        if (datetime.now() - creation_date).total_seconds() > SESSION_TIME_TO_LIVE:
            # Force session reset
            reset = True
            # Save reset time
            per_thread('req_session_time', lambda: datetime.now(), True)

    if SESSION_TIME_TO_LIVE == 0:
        # Session is one-time use
        return requests.sessions.Session()
    else:
        # Session lives some time or forever once created. Default
        return per_thread('req_session', lambda: session if session else requests.sessions.Session(), reset)

def make_request(url: str, timeout: int = 60) -> dict:
    result = _get_req_session().request(
        method="get",
        url=url,
        timeout=timeout
    )
    return result.json()