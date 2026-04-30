def split_documents(documents, chunk_size=300, overlap=50):
    texts = []
    metadata = []

    for doc in documents:
        content = doc["content"]
        path = doc["path"]

        start = 0
        while start < len(content):
            end = start + chunk_size
            chunk = content[start:end]

            texts.append(chunk)
            metadata.append({"source": path})

            start += chunk_size - overlap

    return texts, metadata