from api.auth import generate_token
CLIENT: str = "navidrome-utils"
VERSION: str = "1.13.1"


def get_static_params(user: str, password: str) -> dict[str, str]:
    [auth, salt] = generate_token(password)
    return {
        "u": user,
        "f": "json",
        "c": CLIENT,
        "v": VERSION,
        "t": auth,
        "s": salt
    }