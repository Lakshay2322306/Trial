from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI()
translator = Translator()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str
    dest_lang: str = "en"

@app.post("/translate")
def translate_text(req: TextRequest):
    try:
        translated = translator.translate(req.text, dest=req.dest_lang)
        return {
            "original": req.text,
            "translated": translated.text,
            "detected_source": translated.src
        }
    except Exception as e:
        return {"error": str(e)}
