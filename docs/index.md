# Welcome to Vargur API SDK

Vargur API SDK is a powerful toolkit for building extensible applications with plugin support. It provides a core set of features including mock implementations for database integration, caching, event bus, and authentication, along with a plugin system that allows easy extension of functionality.

## Features

- Plugin system for easy extensibility
- Mock implementations for core components:
  - Database integration
  - Caching
  - Event bus
  - Authentication
- Minimal dependencies for flexibility in implementation

## Getting Started

To get started with Vargur SDK, follow these simple steps:

1. Install the SDK:
   ```
   pip install vargur-sdk
   ```

2. Import the necessary components:
   ```python
   from vargur_sdk import Plugin, load_plugins, event_bus
   ```

3. Create your first plugin:
   ```python
   class MyPlugin(Plugin):
       def __init__(self):
           super().__init__("my_plugin")
           self.router.add_api_route("/hello", self.hello)

       async def hello(self):
           return {"message": "Hello from my plugin!"}
   ```

4. Use the plugin in your application:
   ```python
   app = FastAPI()
   plugins = load_plugins()
   plugins["my_plugin"] = MyPlugin()

   for plugin in plugins.values():
       app.include_router(plugin.router)
   ```

For more detailed information on how to use the SDK and create plugins, check out our [User Guide](user-guide.md).

## API Reference

For detailed information about the SDK's components and functions, see the [API Reference](api-reference.md).

## Creating Plugins

If you're interested in creating plugins for the Vargur SDK, don't miss our [Plugin Guidelines](plugin-guidelines.md). This guide provides best practices and detailed instructions on how to structure and implement your plugins.

## Contributing

Contributions to the Vargur SDK are welcome! Whether it's improving documentation, adding new features, or reporting bugs, your help is appreciated. Please see our contributing guidelines for more information on how to get started.

## License

Vargur SDK is released under the [MIT License](LICENSE).