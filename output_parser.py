from langchain.schema import BaseOutputParser

class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(",")
    

print(CommaSeparatedListOutputParser().parse("apple, banana, cherry"))  # Output: ['apple', 'banana', 'cherry']