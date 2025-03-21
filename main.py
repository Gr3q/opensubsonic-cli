from typer_di import TyperDI

from cli.commands.get_playlists import get_playlists_typer
from cli.commands.get_playlist import get_playlist_typer
from cli.commands.utils import utils_commands


app = TyperDI()

app.add_typer(get_playlists_typer)
app.add_typer(get_playlist_typer)
app.add_typer(utils_commands, name="utils")

if __name__ == "__main__":
    app()
