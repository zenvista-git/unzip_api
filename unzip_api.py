# unzip_api.py
from fastapi import FastAPI, Request
import base64, zipfile, io

app = FastAPI()

@app.post("/unzip")
async def unzip_file(req: Request):
    body = await req.json()
    zip_base64 = body['zip']
    zip_bytes = base64.b64decode(zip_base64)
    zip_io = io.BytesIO(zip_bytes)

    with zipfile.ZipFile(zip_io, 'r') as zip_ref:
        output = {}
        for file_name in zip_ref.namelist():
            if not file_name.endswith("/"):
                content = zip_ref.read(file_name)
                output[file_name] = content.decode("utf-8")  # assumes text

    return output
