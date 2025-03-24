from typing import Literal
from pydantic import BaseModel

class Child(BaseModel):
    id: str
    '''The id of the media'''
    parent: str | None = None
    isDir: bool
    title: str
    album: str | None = None
    artist: str | None = None
    track: int | None = None
    year: int | None = None
    genre: str | None = None
    coverArt: str | None = None
    size: int | None = None
    contentType: str | None = None
    suffix: str | None = None
    transcodedContentType: str | None = None
    transcodedSuffix: str | None = None
    duration: int | None = None 
    bitRate: int | None = None
    bitDepth: int | None = None
    samplingRate: int | None = None
    channelCount: int | None = None
    path: str | None = None
    isVideo: bool | None = None
    userRating: int | None = None
    averageRating: float | None = None
    playCount: int | None = None
    discNumber: int | None = None
    created: str | None = None
    starred: str | None = None
    albumId: str | None = None
    artistId: str | None = None
    type: Literal["music", "podcast", "audiobook", "video"] | None = None
    mediaType: Literal["song", "album", "artist"] | None = None
    bookmarkPosition: int | None = None
    originalWidth: int | None = None
    originalHeight: int | None = None
    played: str | None = None
    bpm: int | None = None
    comment: str | None = None
    sortName: str | None = None
    musicBrainzId: str | None = None
    # genres: list[ItemGenre] | None = None
    # artists: list[ArtistID3] | None = None
    displayArtist: str | None = None
    # albumArtists: list[ArtistID3] | None = None
    displayAlbumArtist: str | None = None
    # contributors: list[Contributor] | None = None
    displayComposer: str | None = None
    moods: list[str] | None = None
    # replayGain: list[ReplayGain] | None = None
    explicitStatus: Literal["explicit", "clean", ""] | None = None