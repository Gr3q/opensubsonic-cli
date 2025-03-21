

from typing import Any
from httpx import Client

from lib.exception import BadHTTPResponse

def get_playlists(
    client: Client
) -> Any:
    ''' Get all playlists you have access to. '''
    response = client.get(
        f"/rest/getPlaylists",
    )
    
    if (response.status_code != 200):
        raise BadHTTPResponse(response)
    
    # TODO: payload validation
    payload = response.json()
    return payload