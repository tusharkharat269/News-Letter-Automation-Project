from langchain_tavily import TavilySearch

search_tool = TavilySearch(max_results=15,time_range="week")

politics_query = """
Latest and most important political and government news worldwide.
Focus on elections, new laws, international relations, government policies, and diplomacy.
"""

business_query = """
Latest updates in business, economy, and finance.
Include stock markets, corporate earnings, global trade, inflation, investments, and startups.
"""

tech_query = """
Top technology news today.
Focus on AI, big tech companies, cybersecurity, software, hardware, space technology, and major product launches.
"""

sports_query = """
Latest sports news highlights.
Cover international tournaments, cricket, football, tennis, Olympic sports, player records, and major sporting events.
"""

entertainment_query = """
Latest news in entertainment, celebrities, and lifestyle.
Include movies, TV, music, fashion, pop culture, celebrity updates, and lifestyle trends.
"""

crime_query = """
Most recent and important crime, law, and justice news.
Include court rulings, criminal cases, law enforcement updates, and public safety issues.
"""
