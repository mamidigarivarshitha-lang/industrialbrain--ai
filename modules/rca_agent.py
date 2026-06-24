from modules.openrouter_helper import ask_llm

def analyze_failure(issue):

    prompt = f"""
You are an industrial maintenance expert.

Equipment Issue:
{issue}

Provide:

1. Probable Root Causes
2. Recommended Actions
3. Confidence Score (0-100)

Keep response concise.
"""

    return ask_llm(prompt, "")