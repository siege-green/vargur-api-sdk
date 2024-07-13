from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    """
    Represents a user in the system.
    """
    id: int
    username: str
    main_character_id: Optional[int] = None


class Character(BaseModel):
    """
    Represents a character in the game.
    """
    id: int
    character_id: int
    character_name: str
    user_id: int
