from httpx import Client
from typer_di import Depends, TyperDI

from cli.deps import http_client
from api.calls.get_playlist import get_playlist as get_playlist_api
from api.calls.star import star

add_playlist_to_favorites_typer = TyperDI()

@add_playlist_to_favorites_typer.command()
def add_playlist_to_favorites(
    id: str,
    client: Client = Depends(http_client)
) -> None:
    '''Add songs from a playlist to the favorites list in the same order it's in the playlist.
    
       It does not check if the songs are already in the favorites list, it will just add all missing.
       If you want to remove the songs included in a playlist from the favorites list, do that with `remove_playlist_to_favorites`.
       
       TODO: Ask if you want to proceed if some songs are already in the favorites list.
    '''
    
    playlist = get_playlist_api(id, client=client)   
    if (playlist.entry is None):
        print("Playlist has no entries")
        return
    
    ids = list(map(lambda x: x.id, reversed(playlist.entry)))
    
    # batches of 100 because the URL can be too big
    split_id_lists = [ids[i:i + 100] for i in range(0, len(ids), 100)]
    for split_ids in split_id_lists:
        star(split_ids, client=client)