from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):

    BOT_TOKEN: SecretStr
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    API_TOKEN: str

    GROUP_ID: str

# postgresql+asyncpg://postgres:qwerty47@localhost/notdb

    @property
    def DATABASE_URL(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='./env/main.env', env_file_encoding='utf-8')

config = Settings()