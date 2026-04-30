from langchain_community.llms import Ollama

def build_qa_chain(vectorstore):
    llm = Ollama(model="tinyllama")

    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    def ask(query):
        docs = retriever.invoke(query)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a STRICT codebase assistant.

Rules:
- Answer ONLY using the provided code
- Do NOT use general knowledge
- If answer not found, say: "Not found in codebase"
- Explain in simple terms
- Mention function names and file names

Context:
{context}

Question:
{query}

Answer:
"""

        response = llm.invoke(prompt)
        return response

    return ask