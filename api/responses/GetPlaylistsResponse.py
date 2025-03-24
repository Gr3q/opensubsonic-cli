from pydantic import AliasPath, BaseModel, Field
from api.models.Playlists import Playlists
from api.models.Response import SubsonicFailedResponse, SubsonicSuccessResponse

class GetPlaylistsSubsonicSuccessResponse(SubsonicSuccessResponse):
    playlists: Playlists
    
class GetPlaylistsSubsonicFailedResponse(SubsonicFailedResponse):
    pass  

class GetPlaylistsResponse(BaseModel):
    subsonicResponse: GetPlaylistsSubsonicSuccessResponse | GetPlaylistsSubsonicFailedResponse = Field(validation_alias=AliasPath('subsonic-response'))