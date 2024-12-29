from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from models import FileMetadata
from background_tasks import process_file


async def upload_file(file: UploadFile, db: Session):
    max_size = 5 * 1024 * 1024  # 5 MB
    file_size = len(await file.read())
    await file.seek(0)  # Reset file pointer after reading

    if file_size > max_size:
        raise HTTPException(status_code=400, detail="File size exceeds 5MB limit")

    metadata = FileMetadata(
        filename=file.filename,
        content_type=file.content_type,
        size=file_size,
    )
    db.add(metadata)
    db.commit()
    db.refresh(metadata)

    # Background processing
    await process_file(file, metadata.id)

    return {"message": "File uploaded successfully", "file_id": metadata.id}

