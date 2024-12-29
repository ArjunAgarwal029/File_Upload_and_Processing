from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class FileMetadata(Base):
    __tablename__ = "file_metadata"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    size = Column(Float, nullable=False)
    upload_time = Column(DateTime, default=datetime.utcnow)
