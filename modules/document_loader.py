import os

def load_documents(folder_path):

    documents = []

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                documents.append({
                    "filename": filename,
                    "content": content
                })

            except Exception as e:
                print(f"Error reading {filename}: {e}")

    return documents