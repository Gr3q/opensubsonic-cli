from typing import Literal
from pydantic import AliasPath, BaseModel, Field

from models.Error import SubsonicError
class SubsonicBaseResponse(BaseModel):
    version: str
    type: str
    serverVersion: str
    openSubsonic: bool

class SubsonicSuccessResponse(BaseModel):
    status: Literal["ok"]

class SubsonicFailedResponse(BaseModel):
    status: Literal["failed"]
    version: str
    type: str
    serverVersion: str
    openSubsonic: bool
    error: SubsonicError
    
type SubsonicResponse = SubsonicSuccessResponse | SubsonicFailedResponse
    
class Response(BaseModel):
    subsonicResponse: SubsonicResponse = Field(validation_alias=AliasPath('subsonic-response'))