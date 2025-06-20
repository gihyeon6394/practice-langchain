from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("what is the capital of {country}?")
prompt_output = prompt.format(country="France")
print(prompt_output)  # Output: "what is the capital of France?"

from langchain.prompts.chat import ChatPromptTemplate

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template), # role
    ("user", human_template) # content
])

chat_prompt_output = chat_prompt.format_messages(
    input_language="English",
    output_language="French",
    text="Hello, how are you?"
)
print(chat_prompt_output)  # Output: [SystemMessage(...), HumanMessage(...)]

from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI()
print(chat_model.invoke(chat_prompt_output))  # Invokes the chat model with the formatted messages