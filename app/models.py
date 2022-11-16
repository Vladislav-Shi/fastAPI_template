from pydantic import BaseModel


class RouteDescription(BaseModel):
    summary: str
    description: str


class PostgresConnectionConfig(BaseModel):
    host: str
    port: int
    database: str
    user: str
    password: str


class LoggingConfig(BaseModel):
    level: int
    format: str
