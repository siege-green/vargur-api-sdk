import aioredis

from .config import config


class Cache:
    def __init__(self):
        self.redis = aioredis.from_url(config.CACHE_URL)

    async def get(self, key: str):
        return await self.redis.get(key)

    async def set(self, key: str, value: str, expire: int = None):
        await self.redis.set(key, value, ex=expire)

    async def delete(self, key: str):
        await self.redis.delete(key)


cache = Cache()
