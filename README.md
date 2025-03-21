# OpenSubsonic cli

Severely incomplete.

## Requirements

* `uv` installed

## Running the cli

_If you don't trust this tool backup your DB first._

```bash
git clone https://github.com/Gr3q/opensubsonic-cli.git
cd opensubsonic-cli
uv sync
uv run main.py --help
```

Follow the output of the cli for available commands.

## Use as a library

TODO

```python
from lib.client import generate_client
from lib.api.get_playlists import get_playlists
client = generate_client("http://localhost:4040", "admin", "admin")

get_playlists(client=client)
```

## Structure

### CLI

All root level commands map to OpenSubsonic endpoints, `utils` have convenience commands.

### Directory structure

* `models` - OpenSubsonic data models (with pydantic)
* `responses` - OpenSubsonic API endpoint response models (with pydantic)
* `lib` - OpenSubsonic API httpx client
* `cli` - CLI commands

## TODO

* Add pydantic models for all OpenSubsonic data structures
* Add all OpenSubsonic commands
