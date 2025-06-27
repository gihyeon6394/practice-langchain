from langchain_openai import OpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel, Field

model_name = "gpt-3.5-turbo-instruct"
temperature = 0.0
model = OpenAI(model_name=model_name, temperature=temperature)

class Actor(BaseModel):
    name: str = Field(description = "Name of the actor in film")
    films: list[str] = Field(description = "List of films the actor has appeared in")

actor_query = "List five actors and the one random film they have appeared in."
parser = PydanticOutputParser(pydantic_object=Actor)
print(parser.get_format_instructions())

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

_input = prompt.format_prompt(query=actor_query)
output = prompt.invoke(_input.to_string())

m = parser.parse(output)
print("Prompt output : " + str(m))
print("Actor name : " + m.name)
print("Films : " + str(m.films))