from json import JSONDecodeError
from typing import Any
from httpx import Client
from pydantic import ValidationError

from lib.exception import BadHTTPResponse
from models.Playlist import Playlist
from responses.GetPlaylistResponse import GetPlaylistResponse


def get_playlist(
    id: str,
    *,
    client: Client,
) -> Playlist | None:
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
        return result.subsonicResponse.playlist
    except JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        raise e
    except ValidationError as e:
        raise e