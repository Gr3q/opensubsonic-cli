from pydantic import BaseModel
from models.Playlist import Playlist

class Playlists(BaseModel):
    playlist: list[Playlist] 