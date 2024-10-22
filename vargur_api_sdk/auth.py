from fastapi import Depends


async def get_current_user(token: str = Depends(lambda: "mock-token")):
    return {"id": 1, "username": "mock_user"}
