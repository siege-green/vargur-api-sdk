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

The database module provides functions for database operations.

#### Functions

- `get_db()`: Async generator that yields a database session.

```python
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

### Cache

The `Cache` class provides methods for interacting with the Redis cache.

```python
class Cache:
    def __init__(self):
        self.redis = aioredis.from_url(config.CACHE_URL)

    async def get(self, key: str):
        return await self.redis.get(key)

    async def set(self, key: str, value: str, expire: int = None):
        await self.redis.set(key, value, ex=expire)

    async def delete(self, key: str):
        await self.redis.delete(key)
```

### Event Bus

The `EventBus` class provides methods for publishing and subscribing to events.

```python
class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event: str, callback: Callable):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    async def publish(self, event: str, **kwargs):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                if asyncio.iscoroutinefunction(callback):
                    await callback(**kwargs)
                else:
                    callback(**kwargs)
```

### Authentication

The authentication module provides functions for user authentication.

#### Functions

- `get_current_user(token: str, db: AsyncSession)`: Authenticates a user based on their JWT token.

```python
async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user
```

## Utility Functions

### create_access_token

Creates a JWT access token for a user.

```python
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm="HS256")
    return encoded_jwt
```

For more detailed information about using these components and functions, please refer to the [User Guide](user-guide.md).