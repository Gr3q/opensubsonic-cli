from collections.abc import Sequence
from typing import Any

from httpx import Client

from lib.exception import BadHTTPResponse


def star(
    ids: Sequence[str],
    *,
    client: Client,
) -> Any:
    response = client.get(
        f"/rest/star",
        params={
            "id": ids
        }
    )
    
    if (response.status_code != 200):
        raise BadHTTPResponse(response)
    
    data = response.json()
    # TODO: response validation
    return data
    