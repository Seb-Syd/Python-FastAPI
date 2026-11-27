import uuid
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageOps

PROFILE_PICS_DIR = Path("media/profile_pics")

def process_profile_image(content: bytes) -> str:
    with Image.open(BytesIO(content)) as original:
        img = ImageOps.exif_transpose(original) # handles unoriented images

        img = ImageOps.fit(img, (300, 300), method=Image.Resampling.LANCZOS) # resizes and resamples image

        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB") # converts to RGB to support transparency

        filename = f"{uuid.uuid4().hex}.jpg" # generates unique id name
        filepath = PROFILE_PICS_DIR / filename

        PROFILE_PICS_DIR.mkdir(parents=True, exist_ok=True) # makes sure directory exists, creates parents directories

        img.save(filepath, "JPEG", quality=85, optimize=True) # balance between quality and filesize

    return filename # stored in database


def delete_profile_image(filename: str | None) -> None:
    if filename is None:
        return

    filepath = PROFILE_PICS_DIR / filename
    if filepath.exists():
        filepath.unlink()
