from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

print([e.value for e in Language])


separator = RecursiveCharacterTextSplitter.get_separators_for_language(Language.PYTHON)
print(separator)

PYTHON_CODE = """
def hello_world():
    print("Hello, world!")

hello_world()
"""

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0,
)

python_docs = python_splitter.create_documents([PYTHON_CODE])
print(python_docs)

for doc in python_docs:
    print(doc.page_content)
