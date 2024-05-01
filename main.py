from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)


chain = prompt | llm
while True:
    print(chain.invoke(
        {
            "input_language": "English",
            "output_language": "Hindi",
            "input": input("What do you want to Translate"),
        }
    ).content)


