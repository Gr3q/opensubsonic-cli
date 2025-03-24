from json import JSONDecodeError
from typing import Any
from httpx import Client
from pydantic import ValidationError

from api.exception import BadHTTPResponse, SubsonicException
from api.models.Playlist import Playlist
from api.responses.GetPlaylistResponse import GetPlaylistResponse


def get_playlist(
    id: str,
    *,
    client: Client,
) -> Playlist:
    response = client.get(
        "/rest/getPlaylist",
        params={
            "id": id
        }
    )
    
    if (response.status_code != 200):
        raise BadHTTPResponse(response)
    
    try:
        data: Any = response.json()
        result = GetPlaylistResponse(**data)
        if (result.subsonicResponse.status == "failed"):
            raise SubsonicException(result.subsonicResponse.error)
        return result.subsonicResponse.playlist

    except JSONDecodeError as e:
        raise e
    except ValidationError as e:
        raise e