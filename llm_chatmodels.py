from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI()
chat_model = ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage

text = "what is the capital of France?"
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=text)
]

print("LLM Response:")
print(llm(text))

print("Chat Model Response:")
print(chat_model(messages))
