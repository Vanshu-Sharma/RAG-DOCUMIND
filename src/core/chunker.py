from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_text_splitter():

    return RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=500,
        chunk_overlap=100
    )