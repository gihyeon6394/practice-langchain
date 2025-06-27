from langchain.output_parsers.enum import EnumOutputParser
from enum import Enum

class Brand(Enum):
    APPLE = "Apple"
    GOOGLE = "Google"
    MICROSOFT = "Microsoft"

parser = EnumOutputParser(enum=Brand)