import logging
from pathlib import Path

import dotenv
from pydantic import BaseSettings

from app.models import PostgresConnectionConfig, LoggingConfig

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_LEVEL = [
    logging.WARNING,
    logging.DEBUG
]


class Settings(BaseSettings):
    DEBUG: bool
    HOST: str
    PORT: int

    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USER: str
    DB_PASSWORD: str

    class Config:
        env_file = Path(BASE_DIR, 'settings', '.env')
        dotenv.load_dotenv(env_file)

    def create_database_config(self) -> PostgresConnectionConfig:
        return PostgresConnectionConfig(
            database=self.DB_DATABASE,
            host=self.DB_HOST,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            port=self.DB_PORT
        )

    def get_log_level(self) -> int:
        return LOG_LEVEL[self.DEBUG]

    def get_logger_conf(self) -> LoggingConfig:
        return LoggingConfig(
            level=self.get_log_level(),
            format='%(levelname)s:   -   %(message)s  %(funcName)s() %(asctime)s'
        )


settings = Settings()

TORTOISE_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': settings.create_database_config().dict(),
        }
    },
    'apps': {
        'models': {
            'models': ['app.database', 'aerich.models'],
            'default_connection': 'default'
        }
    }
}

LOGGER_CONF = {

}