import os

def load_code_files(directory):
    documents = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()

                    documents.append({
                        "content": content,
                        "path": path
                    })

                except Exception as e:
                    print(f"Error reading {path}: {e}")

    return documents