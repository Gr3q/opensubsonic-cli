from pydantic import BaseModel
from api.models.Child import Child

class Playlist(BaseModel):
    id: str
    '''The id of the playlist'''
    name: str
    '''The name of the playlist'''
    comment: str | None = None
    '''A comment'''
    owner: str | None = None
    '''Owner of the playlist'''
    public: bool | None = None
    '''Whether the playlist is public'''
    songCount: int
    '''Number of songs in the playlist'''
    duration: int
    '''Duration of the playlist in seconds'''
    created: str
    '''When the playlist was created - ISO 8601 date'''
    changed: str
    '''When the playlist was last changed - ISO 8601 date'''
    coverArt: str | None = None
    '''Cover art ID'''
    allowedUser: list[str] | None = None
    '''List of allowed usernames'''
    entry: list[Child] | None = None