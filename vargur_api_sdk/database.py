from sqlalchemy.ext.asyncio import AsyncSession


async def get_db():
    yield AsyncSession()
