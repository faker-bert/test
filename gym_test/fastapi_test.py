import fastapi
from pydantic import BaseModel, Field, validate_model


class Result(BaseModel):
    code: str
    success: bool = Field(default=True, description='成功或失败标志')
    
    