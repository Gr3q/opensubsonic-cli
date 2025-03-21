from pydantic import AliasPath, BaseModel, Field
from models.Playlists import Playlists
from models.Response import SubsonicFailedResponse, SubsonicSuccessResponse

class GetPlaylistsSubsonicSuccessResponse(SubsonicSuccessResponse):
    playlists: Playlists
    
class GetPlaylistsSubsonicFailedResponse(SubsonicFailedResponse):
    pass  

class GetPlaylistsResponse(BaseModel):
    subsonicResponse: GetPlaylistsSubsonicSuccessResponse | GetPlaylistsSubsonicFailedResponse = Field(validation_alias=AliasPath('subsonic-response'))