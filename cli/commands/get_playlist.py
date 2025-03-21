import json
from httpx import Client
from typer_di import Depends, TyperDI
from lib.api.get_playlist import get_playlist as get_playlist_api
from cli.deps import http_client

get_playlist_typer = TyperDI()

@get_playlist_typer.command()
def get_playlist(
    id: str,
    client: Client = Depends(http_client)
) -> None:
    ''' Get the details of a single playlist. '''
    data = get_playlist_api(id, client=client)   
    print(json.dumps(data.model_dump(), indent=4))