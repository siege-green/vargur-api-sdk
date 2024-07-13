import os


class Config:
    DEBUG: bool = os.getenv('VARGUR_DEBUG', 'False').lower() == 'true'
    LOG_LEVEL: str = os.getenv('VARGUR_LOG_LEVEL', 'INFO')
    DATABASE_URL: str = os.getenv('VARGUR_DATABASE_URL', 'sqlite:///./test.db')
    SECRET_KEY: str = os.getenv('VARGUR_SECRET_KEY', 'your-secret-key')

    # Discord plugin settings
    DISCORD_BOT_TOKEN: str = os.getenv('VARGUR_DISCORD_BOT_TOKEN')
    DISCORD_GUILD_ID: int = int(os.getenv('VARGUR_DISCORD_GUILD_ID', '0'))


config = Config()
