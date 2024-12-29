from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
import models
from services import upload_file, get_file_metadata

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

@app.post("/upload/")
async def upload_endpoint(file: UploadFile = File(...), db: Session = Depends(get_db)):
    return await upload_file(file, db)

@app.get("/file/{file_id}")
def file_metadata(file_id: int, db: Session = Depends(get_db)):
    metadata = db.query(models.FileMetadata).filter(models.FileMetadata.id == file_id).first()
    if not metadata:
        raise HTTPException(status_code=404, detail="File not found")
    return metadata
