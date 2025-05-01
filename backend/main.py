from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyA9hyjtRj_1TPdc6UGUsZx1kqKzCSp50gI") 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload/")
async def process_file(file: UploadFile, prompt: str = Form(...)):
    content = await file.read()
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()

    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    response = model.generate_content(f"{prompt}\n\n{text[:10000]}")
    result_html = response.text


    with open("output.html", "w", encoding="utf-8") as f:
        f.write(result_html)


    csv_path = "output.csv"
    json_path = "output.json"


    try:
        df = pd.read_html("output.html")[0]
        df.to_csv(csv_path, index=False)
        df.to_json(json_path, orient="records")
    except Exception:
        try:
            data = json.loads(result_html)
        except Exception:
            data = [{"output": result_html}]
        df2 = pd.DataFrame(data)
        df2.to_csv(csv_path, index=False)
        df2.to_json(json_path, orient="records")

    return {
        "html": "/download/html",
        "csv": "/download/csv",
        "json": "/download/json"
    }



@app.get("/download/html")
async def download_html():
    path = "output.html"
    if not os.path.exists(path):
        return JSONResponse({"error": "File not found"}, status_code=404)
    return FileResponse(path, media_type="text/html", filename="student_residences.html")


@app.get("/download/csv")
async def download_csv():
    path = "output.csv"
    if not os.path.exists(path):
        return JSONResponse({"error": "File not found"}, status_code=404)
    def iterfile():
        with open(path, "rb") as f:
            yield from f
    return StreamingResponse(
        iterfile(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=student_residences.csv"}
    )


@app.get("/download/json")
async def download_json():
    path = "output.json"
    if not os.path.exists(path):
        return JSONResponse({"error": "File not found"}, status_code=404)
    return FileResponse(path, media_type="application/json", filename="student_residences.json")
