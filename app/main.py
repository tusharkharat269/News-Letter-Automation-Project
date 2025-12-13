from fastapi import FastAPI
from app.api import user_controller

app = FastAPI(title="News letter Automation")

app.include_router(user_controller.router)

@app.get("/")
async def home():
    return {"message": "hello world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000, reload=True)