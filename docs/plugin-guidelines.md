# Plugin Guidelines for Vargur SDK

This guide provides instructions and best practices for creating plugins using the Vargur SDK.

## Table of Contents

1. [Plugin Structure](#plugin-structure)
2. [Creating a Plugin](#creating-a-plugin)
3. [Plugin Routing](#plugin-routing)
4. [Using SDK Components](#using-sdk-components)
5. [Best Practices](#best-practices)
6. [Integration with Core SDK](#integration-with-core-sdk)

## Plugin Structure

A typical plugin structure in Vargur SDK looks like this:

```
my_plugin/
├── __init__.py
├── main.py
├── models.py
└── routes/
    ├── __init__.py
    ├── route1.py
    └── route2.py
```

- `__init__.py`: Initializes the plugin
- `main.py`: Contains the main plugin class
- `models.py`: Defines any data models used by the plugin
- `routes/`: A directory containing route definitions

## Creating a Plugin

To create a plugin, follow these steps:

1. Create a new directory for your plugin.
2. Create a `main.py` file with a class that inherits from `vargur_sdk.Plugin`:

```python
from vargur_sdk import Plugin

class MyPlugin(Plugin):
    def __init__(self):
        super().__init__("my_plugin")
        # Initialize your plugin here
```

3. In the `__init__.py` file, create an instance of your plugin:

```python
from .main import MyPlugin

plugin = MyPlugin()
```

## Plugin Routing

Use the `self.router` attribute to add routes to your plugin:

```python
from fastapi import APIRouter

class MyPlugin(Plugin):
    def __init__(self):
        super().__init__("my_plugin")
        self.router.add_api_route("/hello", self.hello_world)

    async def hello_world(self):
        return {"message": "Hello from MyPlugin!"}
```

## Using SDK Components

Vargur SDK provides several components that you can use in your plugins:

- **Config**: Access configuration settings
- **Database**: Perform database operations
- **Cache**: Use caching functionality
- **EventBus**: Publish and subscribe to events
- **Authentication**: Implement user authentication

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

## Best Practices

1. **Modularity**: Keep your plugin code modular and well-organized.
2. **Error Handling**: Implement proper error handling and provide meaningful error messages.
3. **Documentation**: Document your plugin's features, configuration options, and usage instructions.
4. **Testing**: Write unit tests for your plugin to ensure reliability.
5. **Performance**: Optimize your plugin for performance, especially if it performs resource-intensive operations.

## Integration with Core SDK

When integrating your plugin with the core Vargur SDK:

1. Use the provided abstract base classes and interfaces.
2. Conform to the SDK's naming conventions and coding style.
3. Utilize the SDK's built-in components (e.g., event bus, caching) when appropriate.
4. Ensure your plugin doesn't interfere with other plugins or the core SDK functionality.

Remember, the current implementation of Vargur SDK uses mock objects. When developing your plugin, you may need to replace these with actual implementations or extend the mock objects based on your specific requirements.

For more detailed information about the SDK components and their usage, refer to the [API Reference](api-reference.md).