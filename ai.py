from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema import Document
from prompt import prompt_kuakua, prompt_rainbow

async def ai_kuakua(base: str) -> str:
    result = ""
    model = ChatOpenAI(model="gpt-3.5-turbo")
    prompt = ChatPromptTemplate.from_template(prompt_kuakua)
    chain = prompt | model | StrOutputParser()
    # result_str = show_search(query=question, db=vectorstore)
    result = chain.invoke({"base": base})
    return result

async def ai_rainbow(base: str) -> str:
    result = ""
    model = ChatOpenAI(model="gpt-3.5-turbo")
    prompt = ChatPromptTemplate.from_template(prompt_rainbow)
    chain = prompt | model | StrOutputParser()
    # result_str = show_search(query=question, db=vectorstore)
    result = chain.invoke({"base": base})
    return result