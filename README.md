# Vargur SDK

Vargur SDK is a powerful toolkit for building extensible applications with plugin support. It provides a core set of features including database integration, caching, event bus, and authentication, along with a plugin system that allows easy extension of functionality.

## Features

- Plugin system for easy extensibility
- Database integration with SQLAlchemy
- Redis-based caching
- Event bus for inter-plugin communication
- JWT-based authentication
- Discord integration plugin

## Installation

You can install Vargur SDK using pip:

```
pip install vargur_sdk
```

## Usage

Here's a basic example of how to use Vargur SDK:

```python
from fastapi import FastAPI
from vargur_sdk import load_plugins, event_bus

app = FastAPI()

# Load all plugins
plugins = load_plugins()

# Include plugin routers
for plugin in plugins.values():
    app.include_router(plugin.router)

# Example of using the event bus
@app.post("/update_user_groups")
async def update_user_groups(user_id: int, groups: List[str]):
    await event_bus.publish("user_groups_changed", user_id=user_id)
    return {"message": "User groups updated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Creating Plugins

To create a plugin, create a new directory in the `plugins` folder with the following structure:

```
plugins/
└── my_plugin/
    ├── __init__.py
    ├── main.py
    └── models.py
```

In `main.py`, define your plugin class:

```python
from vargur_sdk import Plugin

class MyPlugin(Plugin):
    def __init__(self):
        super().__init__("my_plugin")
        self.router.add_api_route("/hello", self.hello)

    async def hello(self):
        return {"message": "Hello from my plugin!"}

plugin = MyPlugin()
```

## Configuration

Vargur SDK uses environment variables for configuration. Here are the available options:

- `VARGUR_DEBUG`: Enable debug mode (default: False)
- `VARGUR_LOG_LEVEL`: Logging level (default: INFO)
- `VARGUR_DATABASE_URL`: Database URL (default: sqlite:///./test.db)
- `VARGUR_CACHE_URL`: Redis cache URL (default: redis://localhost)
- `VARGUR_SECRET_KEY`: Secret key for JWT encoding
- `VARGUR_DISCORD_BOT_TOKEN`: Discord bot token
- `VARGUR_DISCORD_GUILD_ID`: Discord guild ID

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.