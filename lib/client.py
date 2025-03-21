from httpx import Client

from lib.params import get_static_params

def generate_client(base_url: str, user: str, pw: str) -> Client:
    client = Client(base_url=base_url, params=get_static_params(user, pw))
    return client