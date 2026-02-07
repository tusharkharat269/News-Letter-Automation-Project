# News Letter Automation System

A scalable, production-ready news aggregation and newsletter generation system that fetches news from multiple sources, categorizes them, stores them in a database, and provides APIs for customized newsletters.

## Features

- **Multi-Source News Fetching**: Extensible architecture supporting multiple search sources (currently Tavily, designed for easy extension)
- **10 News Categories**: Politics, Business/Economy/Finance, Sports, Science & Technology, Health, World/International, National, Crime/Law, Environment, Entertainment/Lifestyle/Culture
- **Database Storage**: PostgreSQL database with proper schema for news articles and user preferences
- **RESTful APIs**: Comprehensive API endpoints for news retrieval and newsletter generation
- **User Customization**: Users can select preferred categories for personalized newsletters
- **Scalable Architecture**: Industry-standard code structure with separation of concerns

## Project Structure

```
News-Letter-Automation/
├── app/
│   ├── api/                    # API endpoints
│   │   ├── news_controller.py  # News-related endpoints
│   │   └── user_controller.py  # User management endpoints
│   ├── core/                    # Core abstractions
│   │   └── search_base.py      # Abstract base for search tools
│   ├── db/                      # Database configuration
│   │   └── init_db.py          # Database setup and session management
│   ├── dto/                     # Data Transfer Objects
│   │   ├── news_dto.py         # News-related DTOs
│   │   └── user_dto.py         # User-related DTOs
│   ├── model/                   # Database models
│   │   ├── News_model.py       # NewsArticle model
│   │   └── User_model.py       # User model
│   ├── schemas/                 # Pydantic schemas
│   │   ├── news_schema.py      # News data schemas
│   │   └── news_prompts.py     # LLM prompts for each category
│   ├── service/                 # Business logic services
│   │   ├── news_fetch_service.py    # News fetching service
│   │   ├── news_db_service.py       # Database operations for news
│   │   ├── llm_service.py          # LLM integration
│   │   └── webSearch_service.py    # Legacy web search (deprecated)
│   ├── utils/                    # Utility functions
│   │   └── scheduler.py        # Scheduled news fetching
│   ├── agents/                  # LangGraph agents (legacy)
│   ├── config.py                # Configuration
│   └── main.py                 # FastAPI application entry point
├── docs/                        # Documentation
│   ├── News_categories.md      # News categories definition
│   ├── Search_tools.md         # Search tools documentation
│   └── workflow.md             # System workflow
└── README.md                   # This file
```

## Database Schema

### NewsArticle Table
- `id`: UUID (Primary Key)
- `headline`: String (500 chars)
- `short_summary`: Text
- `source_url`: String (1000 chars, unique)
- `category`: Enum (NewsCategory)
- `fetched_at`: DateTime
- `published_date`: DateTime (nullable)
- `source_name`: String (100) - e.g., "tavily"
- `search_query`: String (500, nullable)
- `rank`: Integer - Ranking within category for the day
- `date_key`: String (20) - Format: YYYY-MM-DD

### User Table
- `id`: UUID (Primary Key)
- `name`: String (30)
- `email`: String (100, unique)
- `phone`: String (15, unique)
- `categories`: Array of NewsCategory
- `languages`: String (20)

## API Endpoints

### News Endpoints (`/news`)

1. **GET `/news/category/{category}`**
   - Get top 5 news articles for a specific category
   - Query params: `date_key` (optional), `limit` (default: 5)

2. **GET `/news/categories`**
   - Get news for multiple categories
   - Query params: `categories` (list), `date_key` (optional), `limit_per_category` (default: 5)

3. **GET `/news/all`**
   - Get news for all categories
   - Query params: `date_key` (optional), `limit_per_category` (default: 5)

4. **POST `/news/newsletter`**
   - Generate customized newsletter
   - Body: `NewsletterRequest` with categories and optional date_key

5. **POST `/news/fetch`**
   - Fetch news from sources and save to database
   - Body: `NewsFetchRequest` with optional categories and save_to_db flag

### User Endpoints (`/users`)

1. **POST `/users/`**
   - Create a new user
   - Body: `UserCreate` with name, email, phone, categories, languages

2. **GET `/users/`**
   - Get all users

3. **GET `/users/{user_id}`**
   - Get user by ID

4. **GET `/users/{user_id}/newsletter`**
   - Get customized newsletter for a user based on their preferences
   - Query params: `date_key` (optional)

## Setup

### Prerequisites
- Python 3.8+
- PostgreSQL database
- Environment variables (see `.env.example`)

### Environment Variables
```env
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
USER=postgres_user
PASSWORD=postgres_password
HOST=localhost
PORT=5432
DBNAME=newsletter_db
```

### Installation
```bash
pip install -r requirements.txt
```

### Database Setup
The database tables are automatically created when the application starts (see `app/dto/user_dto.py`).

## Usage

### Running the Application
```bash
python -m app.main
# or
uvicorn app.main:app --reload
```

### Fetching Daily News
```python
from app.utils.scheduler import fetch_daily_news

# Fetch news for all categories
result = fetch_daily_news()

# Fetch news for specific categories
from app.schemas.news_schema import NewsCategory
result = fetch_daily_news(categories=[NewsCategory.POLITICS, NewsCategory.SPORTS])
```

### Scheduled News Fetching
Set up a cron job or use a task scheduler (Celery, APScheduler, etc.) to call `fetch_daily_news()` daily:

```bash
# Example cron job (runs daily at 6 AM)
0 6 * * * cd /path/to/project && python -m app.utils.scheduler
```

## Extending Search Sources

The system is designed to easily add new search sources. To add a new source:

1. Create a new class inheriting from `SearchToolBase` in `app/core/search_base.py`
2. Implement the `search()` and `get_source_name()` methods
3. Add the new tool type to the `create_search_tool()` factory function

Example:
```python
class SerpAPISearchTool(SearchToolBase):
    def search(self, query: str, max_results: int = 15, **kwargs):
        # Implementation
        pass
    
    def get_source_name(self) -> str:
        return "serpapi"
```

## Architecture Highlights

- **Separation of Concerns**: Clear separation between API, service, and data layers
- **Dependency Injection**: Uses FastAPI's dependency injection for database sessions
- **Type Safety**: Comprehensive type hints throughout
- **Error Handling**: Proper exception handling and HTTP status codes
- **Scalability**: Designed to handle multiple search sources and categories
- **Extensibility**: Easy to add new categories, search sources, or features

## Future Enhancements

- [ ] Add more search sources (SerpAPI, Brave Search, MCP tools)
- [ ] Implement caching layer (Redis)
- [ ] Add email newsletter delivery
- [ ] Add news deduplication logic
- [ ] Implement rate limiting
- [ ] Add authentication and authorization
- [ ] Add comprehensive logging
- [ ] Add unit and integration tests
- [ ] Add API documentation with examples

## License

[Your License Here]

