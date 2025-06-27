from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.output_parsers import DatetimeOutputParser
from langchain.prompts import PromptTemplate

output_parser = DatetimeOutputParser()

prompt = PromptTemplate(
    template = "Answer the user question {question}.\n{format_instructions}",
    input_variables=["question"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)
chain = LLMChain(
    prompt=prompt,
    llm=ChatOpenAI(temperature=0.0),
)
output_dict = chain.invoke("around when was bitcoin founded?")
print(output_parser.parse(output_dict['text']))