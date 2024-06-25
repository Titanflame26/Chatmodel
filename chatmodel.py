import os
from langchain_cohere import ChatCohere
#from langchain.schema.messages import HumanMessage, SystemMessage
from langchain_core.messages import HumanMessage,SystemMessage


chat = ChatCohere(cohere_api_key="3ml84htGhfTvj2TffmAB22xNpj6xN6ZLpCkiXNje")

messages = [
    SystemMessage(content="You are Micheal Jordan."),
    HumanMessage(content="Which shoe manufacturer are you associated with?"),
]

response = chat.invoke(messages)
print(response.content)