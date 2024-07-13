class Cache:
    async def get(self, key: str):
        return None

    async def set(self, key: str, value: str, expire: int = None):
        pass

    async def delete(self, key: str):
        pass


cache = Cache()
