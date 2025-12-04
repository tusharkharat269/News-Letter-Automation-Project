import os
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI


BASE_URL = "https://openrouter.ai/api/v1"
API_KEY = os.getenv("OPENROUTER_API_KEY")


# DeepSeek model hosted on OpenRouter
llm = ChatOpenAI(
    model="deepseek/deepseek-chat",  # or "deepseek/deepseek-r1"
    temperature=0.7,
    api_key= API_KEY,
    base_url=BASE_URL,
)

# response = llm.invoke("hi")
# print(response.content)