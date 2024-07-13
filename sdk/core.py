import importlib
import os
from typing import Dict

from fastapi import APIRouter


class Plugin:
    def __init__(self, name: str):
        self.name = name
        self.router = APIRouter(prefix=f"/{name}")


def load_plugins() -> Dict[str, Plugin]:
    plugins = {}
    plugins_dir = os.path.join(os.path.dirname(__file__), '..', 'plugins')
    for plugin_name in os.listdir(plugins_dir):
        plugin_dir = os.path.join(plugins_dir, plugin_name)
        if os.path.isdir(plugin_dir):
            try:
                module = importlib.import_module(f'plugins.{plugin_name}.main')
                plugin = module.plugin
                plugins[plugin_name] = plugin
            except (ImportError, AttributeError) as e:
                print(f"Failed to load plugin {plugin_name}: {e}")
    return plugins
