import os
import sys
import constants
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator


os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY
query = sys.argv[1]


loader = TextLoader("plant-mars-article.txt")
# loader.load()
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))
