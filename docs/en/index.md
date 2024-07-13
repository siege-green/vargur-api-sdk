# Welcome to Vargur API SDK

Vargur API SDK is a powerful tool for developing plugins for the Vargur platform. This documentation will guide you through the process of using the SDK and creating your own plugins.

## Quick Start

To get started with Vargur API SDK, follow these steps:

1. Install the SDK: `pip install vargur-sdk`
2. Import the necessary components in your code:

```python
from vargur_sdk import Plugin, router, task
```

3. Create your plugin class:

```python
class MyPlugin(Plugin):
    def __init__(self):
        super().__init__()

    @task
    async def my_background_task(self):
        # Your background task logic here
        pass

@router.get("/my-endpoint")
async def my_endpoint():
    # Your endpoint logic here
    return {"message": "Hello from my plugin!"}
```

4. Use the plugin in your Vargur application

For more detailed information, please refer to the [User Guide](user-guide.md) and [API Reference](api-reference.md).

## Features

- Easy-to-use plugin system
- Background task support
- Built-in caching and event system
- Database integration
- Multi-language support

## Support

If you encounter any issues or have questions, please check our [GitHub Issues](https://github.com/vargur/vargur-sdk/issues) page or contact our support team.