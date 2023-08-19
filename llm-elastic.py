from elasticsearch import Elasticsearch
from langchain.chat_models import ChatOpenAI
from langchain.chains.elasticsearch_database import ElasticsearchDatabaseChain

#elastic_search_url = "https://<username>:<password>@<host_name_or_ip:<port>/"

#elasticsearch server details
elastic_search_url = "http://elastic:pass123@localhost:9200/"

db = Elasticsearch(elastic_search_url)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
chain = ElasticsearchDatabaseChain.from_llm(llm=llm, database=db, verbose=True)

question = input("Enter your question here  : " )
chain.run(question)

