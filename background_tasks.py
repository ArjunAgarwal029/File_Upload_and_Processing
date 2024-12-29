from fastapi import UploadFile
import asyncio
from utils import resize_image, parse_csv

async def process_file(file: UploadFile, file_id: int):
    await asyncio.sleep(1)  # Simulating async processing
    if file.content_type.startswith("image/"):
        await resize_image(file)
    elif file.content_type == "text/csv":
        await parse_csv(file)
