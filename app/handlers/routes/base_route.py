from fastapi import APIRouter

from app.handlers import descriptions
from app.handlers.models import ResponseModel

router = APIRouter(
    prefix="/base",
    tags=['BASE']
)


@router.get('/', **descriptions.HELLO_WORLD.dict())
async def hello_world() -> ResponseModel:
    response = ResponseModel(status=200, message='hello world!')
    return response
