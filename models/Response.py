from typing import Literal
from pydantic import AliasPath, BaseModel, Field

class SubsonicResponse(BaseModel):
    status: Literal["ok", "failed"]
    version: str
    type: str
    serverVersion: str
    openSubsonic: bool
    # error: Error | None = None
    
class Response(BaseModel):
    subsonicResponse: SubsonicResponse = Field(validation_alias=AliasPath('subsonic-response'))