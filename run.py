import logging

import uvicorn as uvicorn
from tortoise.contrib.fastapi import register_tortoise

from app.app import app
from settings.config import TORTOISE_CONFIG, settings

logging.basicConfig(**settings.get_logger_conf().dict())
logger = logging.getLogger(__name__)


register_tortoise(app=app, config=TORTOISE_CONFIG, generate_schemas=False)

if __name__ == '__main__':
    logger.info(f'swagger url http://{settings.HOST}:{settings.PORT}/docs')
    uvicorn.run(app=app, port=settings.PORT, log_level=settings.get_log_level())
