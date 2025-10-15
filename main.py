from fastapi import FastAPI
from api import user_controller

from service import news_fetch_service

app = FastAPI(title="News letter Automation")

app.include_router(user_controller.router)

@app.get("/")
async def home():
    return {"message": "hello world"}

@app.get("/political_news")
async def get_political_news():
    return news_fetch_service.get_political_news()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000, reload=True)