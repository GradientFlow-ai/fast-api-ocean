from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

from api.t_SNE import fit_tsne

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello from Fastapi, we are cooking now!!"}

@app.post("/tsne")
async def tsne(request: Request):
    partially_extracted_json = await request.json()
    target_array_as_string = partially_extracted_json['data']

    # Convert string to array
    target_array = json.loads(target_array_as_string)
    return fit_tsne(target_array)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
