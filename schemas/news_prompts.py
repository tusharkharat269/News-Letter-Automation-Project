from langchain.prompts import PromptTemplate

politics_prompt = PromptTemplate(
    input_variables=["results"],
    template="""
You are a professional current affairs researcher focusing on politics and government.
Analyze the following search results about politics and governance carefully:

{results}

Task:
- Identify the 5 most important political/government news items.
- Prioritize based on global/national significance, policy impact, elections, diplomacy, and governance.
- Return only a valid JSON list of exactly 5 items in this format:
[
  {{"headline": "...", "short_summary": "...", "source_url": "..."}},
  ...
]
"""
)

business_prompt = PromptTemplate(
    input_variables=["results"],
    template="""
You are a professional current affairs researcher specializing in business, economy, and finance.
Analyze the following search results about markets, companies, trade, and economy:

{results}

Task:
- Select the 5 most significant news items with the highest economic or financial impact.
- Consider stock markets, trade policies, company earnings, economic outlooks, startups, and finance.
- Return only a valid JSON list of exactly 5 items in this format:
[
  {{"headline": "...", "short_summary": "...", "source_url": "..."}},
  ...
]
"""
)


tech_prompt = PromptTemplate(
    input_variables=["results"],
    template="""
You are a professional current affairs researcher focused on technology and innovation.
Analyze the following search results related to technology:

{results}

Task:
- Select the 5 most important technology news items.
- Prioritize AI, cybersecurity, big tech companies, product launches, scientific innovations, and space-tech.
- Return only a valid JSON list of exactly 5 items in this format:
[
  {{"headline": "...", "short_summary": "...", "source_url": "..."}},
  ...
]
"""
)


sports_prompt = PromptTemplate(
    input_variables=["results"],
    template="""
You are a professional sports analyst and researcher.
Analyze the following sports news search results:

{results}

Task:
- Select the 5 most important sports news items.
- Prioritize major tournaments, match outcomes, player milestones, controversies, and international sports updates.
- Return only a valid JSON list of exactly 5 items in this format:
[
  {{"headline": "...", "short_summary": "...", "source_url": "..."}},
  ...
]
"""
)


entertainment_prompt = PromptTemplate(
    input_variables=["results"],
    template="""
You are a professional researcher focusing on entertainment, celebrities, and lifestyle.
Analyze the following entertainment and lifestyle search results:

{results}

Task:
- Select the 5 most relevant and impactful entertainment/celebrity/lifestyle news items.
- Prioritize global entertainment releases, celebrity updates, cultural events, fashion, and lifestyle trends.
- Return only a valid JSON list of exactly 5 items in this format:
[
  {{"headline": "...", "short_summary": "...", "source_url": "..."}},
  ...
]
"""
)


crime_prompt = PromptTemplate(
    input_variables=["results"],
    template="""
You are a professional researcher focusing on crime, law, and justice.
Analyze the following news results about crime and legal matters:

{results}

Task:
- Select the 5 most critical crime/law/justice news items.
- Prioritize court rulings, high-profile cases, criminal investigations, public safety issues, and law enforcement actions.
- Return only a valid JSON list of exactly 5 items in this format:
[
  {{"headline": "...", "short_summary": "...", "source_url": "..."}},
  ...
]
"""
)

