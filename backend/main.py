from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/extract-character")
async def extract_character(file: UploadFile = File(...)):
    original_bytes = await file.read()

    try:
        processed_bytes = remove(original_bytes)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"rembg failed: {str(e)}"},
        )

    try:
        img = Image.open(BytesIO(processed_bytes)).convert("RGBA")
        buf = BytesIO()
        img.save(buf, format="PNG")
        final_bytes = buf.getvalue()
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"PIL failed: {str(e)}"},
        )

    b64 = base64.b64encode(final_bytes).decode("utf-8")

    return {"image_base64": b64}
