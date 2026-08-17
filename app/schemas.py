from pydantic import BaseModel, ConfigDict, Field


class AnalyzeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job_description: str = Field(min_length=20)
    candidate_profile: str = Field(min_length=20)


class AnalyzeResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    overall_fit_score: int = Field(ge=0, le=100)
    fit_summary: str
    strong_matches: list[str]
    partial_matches: list[str]
    gaps: list[str]
    application_recommendations: list[str]
    interview_focus_areas: list[str]
    evidence_used: list[str]
    confidence_notes: list[str]
