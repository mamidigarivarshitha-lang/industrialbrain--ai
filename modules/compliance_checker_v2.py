from modules.document_loader import load_documents

def check_compliance():

    docs = load_documents("data/raw")

    all_text = ""
    print("NEW CODE RUNNING")

    for doc in docs:
        # Each doc is a dictionary: {"filename": ..., "content": ...}
        content = doc.get("content", "")
        all_text += content + "\n"

    all_text = all_text.lower()

    score = 0
    results = []

    if "safety" in all_text:
        score += 25
        results.append("✓ Safety SOP Found")

    if "inspection" in all_text:
        score += 25
        results.append("✓ Inspection Report Found")

    if "maintenance" in all_text or "failed" in all_text:
        score += 25
        results.append("✓ Maintenance History Found")

    if "next inspection" in all_text:
        score += 25
        results.append("✓ Inspection Schedule Available")

    return score, results