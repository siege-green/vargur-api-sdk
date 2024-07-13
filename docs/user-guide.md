# User Guide

This guide will walk you through the process of creating a plugin using the Vargur API SDK.

## Creating a Plugin

To create a plugin, follow these steps:

1. Create a new Python file for your plugin.
2. Import the necessary components from the Vargur SDK:

```python
from vargur_sdk import Plugin, router, task
```

3. Create a class that inherits from `Plugin`:

```python
class MyPlugin(Plugin):
    def __init__(self):
        super().__init__()
```

4. Add endpoints using the `router` decorator:

```python
@router.get("/my-endpoint")
async def my_endpoint():
    return {"message": "Hello from my plugin!"}
```

5. Add background tasks using the `task` decorator:

```python
@task
async def my_background_task(self):
    while True:
        # Your background task logic here
        await asyncio.sleep(60)  # Run every minute
```

## Using the Cache

The SDK provides a built-in caching system. Here's how to use it:

```python
from vargur_sdk import cache

# Set a value in the cache
await cache.set("my_key", "my_value", expire=3600)  # Expires in 1 hour

# Get a value from the cache
value = await cache.get("my_key")

# Delete a value from the cache
await cache.delete("my_key")
```

## Working with the Database

The SDK provides database integration. Here's a basic example:

```python
from vargur_sdk import get_db
from sqlalchemy.future import select
from your_models import YourModel

@router.get("/db-example")
async def db_example():
    async with get_db() as session:
        result = await session.execute(select(YourModel))
        items = result.scalars().all()
        return {"items": items}
```

For more advanced usage, refer to the [API Reference](api-reference.md).