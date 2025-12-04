from typing import List
from pydantic import BaseModel, Field

class NewsResponse(BaseModel):
    headline: str = Field(description="headline of news in short")
    short_summary: str = Field(description="short summary of news in 2-3 lines")
    source_url: str = Field(description="URL of the news article")

class NewsList(BaseModel):
    items: List[NewsResponse] = Field(description="List of top 5 news articles")