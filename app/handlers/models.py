from pydantic import BaseModel


class BaseResponseModel(BaseModel):
    status: int


class ResponseModel(BaseResponseModel):
    message: str
