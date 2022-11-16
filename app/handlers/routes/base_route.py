from fastapi import APIRouter

from app.handlers import descriptions

router = APIRouter(
    prefix="/base"
)


@router.get('/', **descriptions.HELLO_WORLD.dict())
async def hello_world():
    return {'message': 'hello world!'}
