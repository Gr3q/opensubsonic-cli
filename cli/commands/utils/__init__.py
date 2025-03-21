from typer_di import TyperDI
from .add_playlist_to_favorites import add_playlist_to_favorites_typer


utils_commands = TyperDI()
utils_commands.add_typer(add_playlist_to_favorites_typer)