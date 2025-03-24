

from json import JSONDecodeError
from typing import Any
from httpx import Client
from pydantic import ValidationError

from api.exception import BadHTTPResponse, SubsonicException
from api.models.Playlists import Playlists
from api.responses.GetPlaylistsResponse import GetPlaylistsResponse

def get_playlists(
    client: Client
) -> Playlists:
    ''' Get all playlists you have access to. '''
    response = client.get(
        f"/rest/getPlaylists",
    )
    
    if (response.status_code != 200):
        raise BadHTTPResponse(response)
    
    try:
        data: Any = response.json()
        result = GetPlaylistsResponse(**data)
        if (result.subsonicResponse.status == "failed"):
            raise SubsonicException(result.subsonicResponse.error)
        return result.subsonicResponse.playlists

    except JSONDecodeError as e:
        raise e
    except ValidationError as e:
        raise e