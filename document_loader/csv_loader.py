from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="./csv_sample.csv") # lazy loading
data = loader.load() # loaded
print(data)
"""
name,age,country
Neville Hardy,56,Niue
Dacia Cohen,74,Falkland Islands (Malvinas)
Kathey Daniel,10,Slovenia
Mallie Welch,12,Equatorial Guinea
Katia Bryant,14,Ghana
Laurice Robertson,53,Saudi Arabia
Minh Barrett,27,French Southern Territories
Latashia Perez,52,Finland
Elvina Ross,68,New Zealand
"""

print(data[0].page_content)  # Accessing the content of the first document
"""
name: Neville Hardy
age: 56
country: Niue
"""

print(data[0].metadata)  # Accessing the metadata of the first document
"""
{'source': './csv_sample.csv', 'row_number': 1}
"""

loader = CSVLoader(
    file_path='./csv_sample_no_header.csv',
    csv_args={
        'delimiter': ',',
        'quotechar': '"',
        'fieldnames': ['name', 'age', 'country']
    })

data = loader.load()
print(data[1].page_content)
"""
name: Dacia Cohen
age: 74
country: Falkland Islands (Malvinas)
"""