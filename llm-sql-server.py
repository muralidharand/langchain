from langchain.agents import create_sql_agent 
from langchain.agents.agent_toolkits import SQLDatabaseToolkit 
from langchain.sql_database import SQLDatabase 
from langchain.llms.openai import OpenAI 
from langchain.agents import AgentExecutor 
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
import pandas as pd
import openai
import pymssql
import sqlalchemy
import pyodbc 

SQL_SERVER = "<hostname>.database.windows.net:1433"
SQL_DBNAME = "<database_name>"
SQL_USER = "<username>"
SQL_PWD = "<sql_password>"

llm = ChatOpenAI(temperature=0,model="gpt-3.5-turbo")
sqlconn = f"mssql+pymssql://{SQL_USER}:{SQL_PWD}@{SQL_SERVER}/{SQL_DBNAME}"
db = SQLDatabase.from_uri(sqlconn)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(llm=llm,toolkit=toolkit,verbose=True)
question = input("Enter your question here : ")
answer = agent_executor.run(question)  

