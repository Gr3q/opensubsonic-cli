from pydantic import BaseModel
from api.models.Playlist import Playlist

class Playlists(BaseModel):
    playlist: list[Playlist] 