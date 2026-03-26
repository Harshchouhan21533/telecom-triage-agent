from langchain_community.llms import Ollama

llm = Ollama(model="gemma3:1b")

def classify_query(text):
    prompt = f"""
    Classify the following telecom query into:
    Intent: (billing, network, complaint, recharge, other)
    Urgency: (low, medium, high)

    Query: {text}

    Output format:
    Intent: <intent>
    Urgency: <urgency>
    """

    response = llm.invoke(prompt)
    return response