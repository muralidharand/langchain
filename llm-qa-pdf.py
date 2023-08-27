from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

#Locate your PDF here.
pdf="<YOUR_PDF_GOES_HERE>"
#Load the PDF
loader = PyPDFLoader(pdf)
documents = loader.load()

api_key = "sk-?????"
llm = OpenAI(openai_api_key=api_key)
chain = load_qa_chain(llm,verbose=True)
question = input("Enter your question here : ")
response = chain.run(input_documents=documents, question=question)
print(response) 
