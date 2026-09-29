from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader(
    "../../data/notice.pdf",
)

documents = loader.load()

#문서를 청크로 나누기

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 150,
    chunk_overlap = 30
)

chunks = splitter.split_documents(documents)
 
print(f"{len(chunks)}");
print(f"{chunks[0].page_content}");
print(f"{chunks[1].page_content}");
