from loader import load_code_files
from splitter import split_documents
from embeddings import get_embeddings
from vectorstore import create_vectorstore
from qa_chain import build_qa_chain

def main():
    print("📂 Loading codebase...")
    docs = load_code_files("../data")

    if not docs:
        print("❌ No Python files found in /data folder")
        return

    print("✂️ Splitting documents...")
    texts, metadata = split_documents(docs)

    print("🧠 Creating embeddings...")
    embeddings = get_embeddings()

    print("📦 Building vector store...")
    vectorstore = create_vectorstore(texts, metadata, embeddings)

    print("🤖 Initializing assistant...")
    qa = build_qa_chain(vectorstore)

    print("\n✅ Ready! Ask questions (type 'exit' to quit)\n")

    while True:
        query = input(">> ")

        if query.lower() == "exit":
            print("👋 Exiting...")
            break

        try:
            answer = qa(query)
            print("\n💡 Answer:\n", answer, "\n")

        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()