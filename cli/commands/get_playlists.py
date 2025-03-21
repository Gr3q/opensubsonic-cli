import json
from httpx import Client
from typer_di import Depends, TyperDI

from cli.deps import http_client
from lib.api.get_playlists import get_playlists as get_playlists_api

get_playlists_typer = TyperDI()

@get_playlists_typer.command()
def get_playlists(
    client: Client = Depends(http_client)
) -> None:
    ''' Get all playlists you have access to. '''
    result = get_playlists_api(client=client)
    if result is None:
        print("No data")
        return
    
    print(json.dumps(result, indent=4))