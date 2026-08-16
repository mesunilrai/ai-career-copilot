from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

from app.ai.analyzer import analyze_job
from app.schemas import AnalyzeRequest, AnalyzeResponse

load_dotenv()

app = FastAPI(title="AI Career Copilot", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    try:
        result = analyze_job(request.job_description, request.candidate_profile)
        return AnalyzeResponse.model_validate(result)
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=502, detail="AI response did not match the expected format") from exc
