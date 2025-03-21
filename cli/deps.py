from httpx import Client
import typer

from lib.client import generate_client


def http_client(
    base_url: str = typer.Option(help="The base URL of the Navidrome server, like 'https://navidrome.yourdomain.com'", envvar="NAVIDROME_URL",),
    user: str = typer.Option(help="The username to use for authentication", envvar="NAVIDROME_USER"),
    password: str = typer.Option(help="The password to use for authentication", prompt=True, hide_input=True, envvar="NAVIDROME_PASSWORD"),
) -> Client:
    
    client = generate_client(base_url, user, password)
    # TODO: client cleanup with yield?
    return client