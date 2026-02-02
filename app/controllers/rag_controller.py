from fastapi import APIRouter
from app.models.requests_models import QueryRequest
from app.services.rag_services import get_rag_answer
from app.services.injest import story_embeding

router = APIRouter(prefix="/story", tags=["STORY"])
@router.post("/injest")
def injest_story():
    response = story_embeding()
    return {
        "message" : response
    }


@router.post("/ask")
def ask_policy_question(request: QueryRequest):
    answer = get_rag_answer(request.question)
    return {
        "question": request.question,
        "answer": answer
    }