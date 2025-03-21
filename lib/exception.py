from typing import override
from httpx import Response

class BadHTTPResponse(Exception):
    def __init__(self, response: Response) -> None:
        self.response: Response = response
        super().__init__()

    @override
    def __str__(self) -> str:
        return f"Bad HTTP response: {self.response.status_code} - {self.response.text}"