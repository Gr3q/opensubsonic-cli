from hashlib import md5
import secrets
from typing import NamedTuple

class TokenDetails(NamedTuple):
    token: str
    salt: str


def generate_token(pw: str) -> TokenDetails:
    salt = secrets.token_hex(8)
    token = md5(str.encode(pw + salt))
    return TokenDetails(token.hexdigest(), salt)