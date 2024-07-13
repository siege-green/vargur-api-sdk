# User Guide

This guide will walk you through the process of using the Vargur API SDK to create plugins and build extensible applications.

## Table of Contents

1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Creating a Plugin](#creating-a-plugin)
4. [Using SDK Components](#using-sdk-components)
5. [Configuration](#configuration)
6. [Best Practices](#best-practices)

## Installation

To install Vargur SDK, use pip:

```
pip install vargur_sdk
```

## Basic Usage

Here's a basic example of how to use Vargur SDK:

```python
from fastapi import FastAPI
from vargur_sdk import Plugin, load_plugins, event_bus

app = FastAPI()

# Load all plugins
plugins = load_plugins()

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

## Creating a Plugin

To create a plugin:

1. Create a new Python file for your plugin.
2. Import the necessary components from the Vargur SDK:

```python
from vargur_sdk import Plugin, router
```

3. Create a class that inherits from `Plugin`:

```python
class MyPlugin(Plugin):
    def __init__(self):
        super().__init__("my_plugin")
        self.router.add_api_route("/hello", self.hello_world)

    async def hello_world(self):
        return {"message": "Hello from MyPlugin!"}
```

## Using SDK Components

Vargur SDK provides several mock components that you can use in your plugins:

- **Config**: Access configuration settings
- **Database**: Perform database operations (mock)
- **Cache**: Use caching functionality (mock)
- **EventBus**: Publish and subscribe to events (mock)
- **Authentication**: Implement user authentication (mock)

Example usage:

```python
from vargur_sdk import config, get_db, cache, event_bus, get_current_user

class MyPlugin(Plugin):
    def __init__(self):
        super().__init__("my_plugin")
        self.router.add_api_route("/example", self.example_route)

    async def example_route(self):
        db = await get_db()
        cached_data = await cache.get("my_key")
        await event_bus.publish("my_event", data="Some data")
        return {"message": "Example route"}
```

Note: These components are currently mock implementations. You may need to replace them with actual implementations based on your specific requirements.

## Configuration

You can modify the SDK configuration using the `config` object:

```python
from vargur_sdk import config

config.DEBUG = True
config.LOG_LEVEL = "DEBUG"
config.DATABASE_URL = "your_database_url"
config.SECRET_KEY = "your_secret_key"
```

## Best Practices

1. Keep your plugin code modular and well-organized.
2. Implement proper error handling and provide meaningful error messages.
3. Document your plugin's features, configuration options, and usage instructions.
4. Write unit tests for your plugin to ensure reliability.
5. Optimize your plugin for performance, especially if it performs resource-intensive operations.

For more detailed information about creating plugins, refer to the [Plugin Guidelines](plugin-guidelines.md).