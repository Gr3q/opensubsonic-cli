from collections.abc import Sequence
from json import JSONDecodeError
from typing import Any

from httpx import Client
from pydantic import ValidationError

from lib.exception import BadHTTPResponse, SubsonicException
from models.Response import Response


def star(
    ids: Sequence[str] | None = None,
    albumId: Sequence[str] | None = None,
    artistId: Sequence[str] | None = None,
    *,
    client: Client,
) -> None:
    params: dict[str, Sequence[str]] = {}
    if (ids):
        params["id"] = ids
    if (albumId):
        params["albumId"] = albumId
    if (artistId):
        params["artistId"] = artistId

    response = client.get(
        f"/rest/star",
        params=params
    )
    
    if (response.status_code != 200):
        raise BadHTTPResponse(response)
    
    try:
        data: Any = response.json()
        result = Response(**data)
        if (result.subsonicResponse.status == "failed"):
            raise SubsonicException(result.subsonicResponse.error)

    except JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        raise e
    except ValidationError as e:
        raise e
    