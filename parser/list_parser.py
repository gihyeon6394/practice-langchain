from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate(
    template= "List five {subjects}.\n {format_instructions}",
    input_variables=["subjects"],
    partial_variables={"format_instructions": format_instructions}
)

model = ChatOpenAI(temperature=0.0)

_input = prompt.format(subjects="fruits")
output = model.invoke(_input)
parsed_output = output_parser.parse(output)
print("Prompt output : " + parsed_output)