# API Reference

This page provides detailed information about the key components and functions of the Vargur API SDK.

## Core Components

### Plugin

The `Plugin` class is the base class for all plugins in the Vargur SDK.

```python
class Plugin:
    def __init__(self, name: str):
        self.name = name
        self.router = APIRouter(prefix=f"/{name}")
```

#### Methods

- `__init__(name: str)`: Initializes a new plugin with the given name.

### Config

The `Config` class holds configuration settings for the Vargur SDK.

```python
class Config:
    DEBUG: bool
    LOG_LEVEL: str
    DATABASE_URL: str
    SECRET_KEY: str
    DISCORD_BOT_TOKEN: str
    DISCORD_GUILD_ID: int
```

### Database

The database module provides a mock function for database operations.

#### Functions

- `get_db()`: Async generator that yields a mock database session.

```python
async def get_db():
    # Mock implementation
    yield AsyncSession()
```

### Cache

The `Cache` class provides mock methods for interacting with a cache.

```python
class Cache:
    async def get(self, key: str):
        # Mock implementation
        return None

    async def set(self, key: str, value: str, expire: int = None):
        # Mock implementation
        pass

    async def delete(self, key: str):
        # Mock implementation
        pass
```

### Event Bus

The `EventBus` class provides mock methods for publishing and subscribing to events.

```python
class EventBus:
    def subscribe(self, event: str, callback):
        # Mock implementation
        pass

    async def publish(self, event: str, **kwargs):
        # Mock implementation
        pass
```

### Authentication

The authentication module provides a mock function for user authentication.

#### Functions

- `get_current_user(token: str)`: Returns a mock authenticated user.

```python
async def get_current_user(token: str = Depends(lambda: "mock-token")):
    # Mock implementation
    return {"id": 1, "username": "mock_user"}
```

## Utility Functions

### load_plugins

Loads all available plugins.

```python
def load_plugins():
    # Mock implementation
    return {}
```

Note: All these components and functions are currently mock implementations. They provide the structure and interface of the SDK but do not perform actual operations. When using this SDK, you may need to replace these mock implementations with actual functionality based on your specific requirements.

For more detailed information about using these components and functions, please refer to the [User Guide](user-guide.md).