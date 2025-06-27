from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

response_schemas = [
    ResponseSchema(
        name="answer",
        description="The answer to the question",
    ),
    ResponseSchema(
        name="source",
        description="The source of the answer",
    ),
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

from_instructions = output_parser.get_format_instructions()
    