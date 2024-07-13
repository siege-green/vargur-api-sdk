from fastapi import APIRouter


class Plugin:
    def __init__(self, name: str):
        self.name = name
        self.router = APIRouter(prefix=f"/{name}")


def load_plugins():
    return {}
