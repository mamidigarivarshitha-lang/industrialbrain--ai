from modules.document_loader import load_documents

def check_compliance():

    docs = load_documents("data/raw")
    
    # ADD THIS HERE 👇
    print("\nLoaded files:")
    for doc in docs:
        print(doc.get("filename"))

    all_text = ""
    print("NEW CODE RUNNING")


    for doc in docs:
        content = doc.get("content", "")
        all_text += content + "\n"

    all_text = all_text.lower()

    score = 0
    results = []

    # Safety SOP
    if "safety" in all_text or "sop" in all_text:
        score += 25
        results.append("✓ Safety SOP Found")
    else:
        results.append("✗ Safety SOP Missing")

    # Inspection Report
    if "inspection" in all_text:
        score += 25
        results.append("✓ Inspection Report Found")
    else:
        results.append("✗ Inspection Report Missing")

    # Maintenance History
    if "maintenance" in all_text or "failed" in all_text or "action taken" in all_text:
        score += 25
        results.append("✓ Maintenance History Found")
    else:
        results.append("✗ Maintenance History Missing")

    # Inspection Schedule
    if "next inspection" in all_text:
        score += 25
        results.append("✓ Inspection Schedule Available")
    else:
        results.append("✗ Inspection Schedule Missing")

    return score, results