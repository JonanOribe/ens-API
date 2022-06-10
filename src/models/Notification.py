from pydantic import BaseModel, Field
from src.generics.pyObjectId import PyObjectId
import datetime

class Notification(BaseModel):
    id:PyObjectId = Field(default_factory=PyObjectId,alias="_id")
    client_id: str = Field(...)
    title: str = Field(...)
    text: str = Field(...)
    timestamp: str = Field(...)

    class Config:
        schema_extra = {
            "example":{
                "client_id":"NzIMN8jMOZyVuWktmLMwa1jDvdMqXbc3",
                "title":"Test title",
                "text":"Test text",
                "timestamp":datetime.datetime.now()
            }
        }