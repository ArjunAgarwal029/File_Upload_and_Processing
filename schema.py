from pydantic import BaseModel
from datetime import datetime

class FileMetadataResponse(BaseModel):
    id: int
    filename: str
    content_type: str
    size: float
    upload_time: datetime

    class Config:
        orm_mode = True
