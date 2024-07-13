# Vargur API SDK

Vargur API SDK is a powerful toolkit for building extensible applications with plugin support. It provides a core set of features including database integration, caching, event bus, and authentication, along with a plugin system that allows easy extension of functionality.

## Features

- Plugin system for easy extensibility
- Mock implementations for database integration, caching, event bus, and authentication
- Minimal dependencies for flexibility in implementation

## Installation

You can install Vargur API SDK using pip:

```
pip install vargur-api-sdk
```

## Usage

Here's a basic example of how to use Vargur API SDK:

```python
from fastapi import FastAPI
from vargur_sdk import Plugin, load_plugins, event_bus

app = FastAPI()

class MyPlugin(Plugin):
    def __init__(self):
        super().__init__("my_plugin")
        self.router.add_api_route("/hello", self.hello)

    async def hello(self):
        return {"message": "Hello from my plugin!"}

# Load all plugins
plugins = load_plugins()
plugins["my_plugin"] = MyPlugin()

# Include plugin routers
for plugin in plugins.values():
    app.include_router(plugin.router)

# Example of using the event bus
@app.post("/trigger_event")
async def trigger_event():
    await event_bus.publish("some_event", data="Some data")
    return {"message": "Event triggered"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Components

- **Plugin**: Base class for creating plugins
- **Config**: Configuration settings for the SDK
- **Database**: Mock database session provider
- **Cache**: Mock caching implementation
- **EventBus**: Mock event publishing and subscribing system
- **Authentication**: Mock user authentication

## Configuration

Vargur API SDK uses a `Config` class for configuration. You can modify these settings in your application:

```python
from vargur_sdk import config

config.DEBUG = True
config.LOG_LEVEL = "DEBUG"
config.DATABASE_URL = "your_database_url"
config.SECRET_KEY = "your_secret_key"
```

## Documentation

For more detailed information, please refer to the following documentation:

- [User Guide](https://meloncafe.github.io/vargur-api-sdk/user-guide)
- [API Reference](https://meloncafe.github.io/vargur-api-sdk/api-reference)
- [Plugin Guidelines](https://meloncafe.github.io/vargur-api-sdk/plugin-guidelines)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).