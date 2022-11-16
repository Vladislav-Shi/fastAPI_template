from fastapi import FastAPI

from app.handlers.router import include_routes

app = FastAPI()
include_routes(app)


@app.get('/ping')
async def ping():
    return {'message': 'OK'}
