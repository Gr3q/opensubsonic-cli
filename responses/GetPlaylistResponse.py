from pydantic import AliasPath, BaseModel, Field
from models.Playlist import Playlist
from models.Response import SubsonicResponse

class GetPlaylistSubsonicResponse(SubsonicResponse):
    playlist: Playlist
    
class GetPlaylistResponse(BaseModel):
    subsonicResponse: GetPlaylistSubsonicResponse = Field(validation_alias=AliasPath('subsonic-response'))