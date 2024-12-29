import asyncio
from fastapi import UploadFile


async def resize_image(file: UploadFile):
    # Placeholder for image resizing logic
    await asyncio.sleep(1)  # Simulating processing
    print(f"Image resized: {file.filename}")

async def parse_csv(file: UploadFile):
    # Placeholder for CSV parsing logic
    await asyncio.sleep(1)  # Simulating processing
    print(f"CSV parsed: {file.filename}")
