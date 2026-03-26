from fastapi import FastAPI
from pydantic import BaseModel

from triage.classifier import classify_query
from triage.ner import extract_entities
from triage.responder import generate_response

# ✅ MUST be before any @app
app = FastAPI()

# ✅ Request body
class QueryRequest(BaseModel):
    query: str

# ✅ Simple home route
@app.get("/")
def home():
    return {"message": "Telecom Triage Agent Running"}

# ✅ Chat memory (session-based)
sessions = {}

@app.post("/triage")
def triage(request: QueryRequest, session_id: str = "default"):
    if session_id not in sessions:
        sessions[session_id] = []

    history = sessions[session_id]

    query = request.query
    classification = classify_query(query)
    entities = extract_entities(query)

    # pass history
    response = generate_response(query, classification, entities)

    history.append({
        "user": query,
        "bot": response
    })

    return {
        "query": query,
        "classification": classification,
        "entities": entities,
        "response": response,
        "history": history
    }