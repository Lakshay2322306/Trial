from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = Translator()

class TranslationRequest(BaseModel):
    text: str
    dest_lang: str

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    try:
        result = translator.translate(request.text, dest=request.dest_lang)
        return {
            "original": request.text,
            "translated": result.text,
            "detected_source": result.src
        }
    except Exception as e:
        return {
            "error": str(e)
        }
