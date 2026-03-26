from langchain_community.llms import Ollama

llm = Ollama(model="gemma3:1b")

chat_history = []

def generate_response(query, classification, entities):
    global chat_history

    chat_history.append(f"User: {query}")
    context = "\n".join(chat_history)

    prompt = f"""
You are a telecom support agent.

Conversation so far:
{context}

Latest Query:
{query}

Classification:
{classification}

Entities:
{entities}

Give a helpful and polite response.
"""

    response = llm.invoke(prompt)

    chat_history.append(f"Agent: {response}")

    return response