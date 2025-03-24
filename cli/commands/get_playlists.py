import json
from httpx import Client
from typer_di import Depends, TyperDI

from cli.deps import http_client
from api.calls.get_playlists import get_playlists as get_playlists_api

get_playlists_typer = TyperDI()

@get_playlists_typer.command()
def get_playlists(
    client: Client = Depends(http_client)
) -> None:
    ''' Get all playlists you have access to. '''
    result = get_playlists_api(client=client)    
    print(json.dumps(result.model_dump(), indent=4))