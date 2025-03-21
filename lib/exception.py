from typing import override
from httpx import Response
from models.Error import SubsonicError

class BadHTTPResponse(Exception):
    def __init__(self, response: Response) -> None:
        self.response: Response = response
        super().__init__()

    @override
    def __str__(self) -> str:
        return f"Bad HTTP response: {self.response.status_code} - {self.response.text}"
    
class SubsonicException(Exception):
    def __init__(self, error: SubsonicError) -> None:
        self.error: SubsonicError = error
        super().__init__()

    @override
    def __str__(self) -> str:
        return f"Subsonic error: {self.error.code} - {self.error.message} - {self.error.helpUrl}"