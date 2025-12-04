
from schemas.news_schema import NewsList, NewsResponse
from service.webSearch_service import *
from schemas.news_prompts import *
from service.llm_service import llm


# for sturcture output
llm_struct_op = llm.with_structured_output(NewsList)


def get_political_news() -> NewsResponse:

    search_results = search_tool.invoke(politics_query)
    # Format prompt
    final_prompt = politics_prompt.format(query=politics_query, results=search_results)
    # get llm response
    response = llm_struct_op.invoke(final_prompt)
    return response

def get_business_news() -> NewsList:
    search_results = search_tool.invoke(business_query)
    final_prompt = business_prompt.format(results=search_results)
    return llm_struct_op.invoke(final_prompt)


def get_technology_news() -> NewsList:
    search_results = search_tool.invoke(tech_query)
    final_prompt = tech_prompt.format(results=search_results)
    return llm_struct_op.invoke(final_prompt)


def get_sports_news() -> NewsList:
    search_results = search_tool.invoke(sports_query)
    final_prompt = sports_prompt.format(results=search_results)
    return llm_struct_op.invoke(final_prompt)


def get_entertainment_news() -> NewsList:
    search_results = search_tool.invoke(entertainment_query)
    final_prompt = entertainment_prompt.format(results=search_results)
    return llm_struct_op.invoke(final_prompt)


def get_crime_news() -> NewsList:
    search_results = search_tool.invoke(crime_query)
    final_prompt = crime_prompt.format(results=search_results)
    return llm_struct_op.invoke(final_prompt)