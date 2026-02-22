from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()

MUSIC_FOLDER = "musics"

@app.get("/musics/{music_name}")
def get_music(music_name: str):
    file_path = os.path.join(MUSIC_FOLDER, f"{music_name}.mp3")
    
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="Música não encontrada")
    
    return FileResponse(file_path, media_type="audio/mpeg")