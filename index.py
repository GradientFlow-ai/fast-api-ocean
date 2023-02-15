from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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
    return {"message": "Hello from Fastapi, we are cooking now!"}

@app.get("/tsne")
async def tsne(request: Request):
    return await request.json()

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
