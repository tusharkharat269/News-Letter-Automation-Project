from typing import List
from pydantic import BaseModel, Field
from enum import StrEnum

class NewsResponse(BaseModel):
    headline: str = Field(description="headline of news in short")
    short_summary: str = Field(description="short summary of news in 2-3 lines")
    source_url: str = Field(description="URL of the news article")

class NewsList(BaseModel):
    items: List[NewsResponse] = Field(description="List of top 5 news articles")

class NewsCategory(StrEnum):
    POLITICS = "politics"
    BUSINESS_ECONOMY_FINANCE = "business_economy_finance"
    SPORTS = "sports"
    SCIENCE_TECHNOLOGY = "science_technology"
    HEALTH = "health"
    WORLD_INTERNATIONAL = "world_international"
    NATIONAL = "national"
    CRIME_LAW = "crime_law"
    ENVIRONMENT = "environment"
    ENTERTAINMENT_LIFESTYLE_CULTURE = "entertainment_lifestyle_culture"
    