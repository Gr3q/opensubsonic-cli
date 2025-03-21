from pydantic import AliasPath, BaseModel, Field
from models.Playlist import Playlist
from models.Response import SubsonicFailedResponse, SubsonicSuccessResponse

class GetPlaylistSubsonicSuccessResponse(SubsonicSuccessResponse):
    playlist: Playlist
    
class GetPlaylistSubsonicFailedResponse(SubsonicFailedResponse):
    pass  
class GetPlaylistResponse(BaseModel):
    subsonicResponse: GetPlaylistSubsonicFailedResponse = Field(validation_alias=AliasPath('subsonic-response'))