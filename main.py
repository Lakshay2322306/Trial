from fastapi import FastAPI, Query from fastapi.middleware.cors import CORSMiddleware from pydantic import BaseModel from googletrans import Translator

app = FastAPI()

Allow CORS for frontend on Vercel

app.add_middleware( CORSMiddleware, allow_origins=[""], allow_credentials=True, allow_methods=[""], allow_headers=["*"], )

translator = Translator()

class TranslationRequest(BaseModel): text: str src_lang: str = 'auto' dest_lang: str = 'en'

@app.post("/translate") async def translate(req: TranslationRequest): try: result = translator.translate(req.text, src=req.src_lang, dest=req.dest_lang) return { "original": req.text, "translated": result.text, "source_language": result.src, "destination_language": result.dest } except Exception as e: return {"error": str(e)}

@app.get("/") async def root(): return {"message": "Translation API is running!"}

