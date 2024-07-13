class Config:
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "your-secret-key"
    DISCORD_BOT_TOKEN: str = "mock-discord-token"
    DISCORD_GUILD_ID: int = 123456789


config = Config()
