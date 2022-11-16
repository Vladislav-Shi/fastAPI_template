from app.models import RouteDescription
"""
В данном файле хранится описание всех ручек.
Пример использвания:

@router.get('/', **descriptions.HELLO_WORLD.dict())

"""

HELLO_WORLD = RouteDescription(
    summary='Hello world',
    description='This base rout give message "hello world"'
)
