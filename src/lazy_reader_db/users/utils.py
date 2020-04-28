from typing import Tuple

from src.lazy_reader_db.users.user import User


def tuple_to_user(t: Tuple[int, str, str, bool]) -> User:
    return User(id=t[0], name=t[1], api_key=t[2], deleted=t[3])
