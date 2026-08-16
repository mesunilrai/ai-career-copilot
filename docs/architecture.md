# AI Career Copilot — V1 Architecture

## Goal

Turn a job description and the user's career profile into practical, evidence-based application guidance.

## V1 Scope

1. Job Description input
2. Master Profile input
3. Job Fit analysis
4. Application recommendations
5. Interview preparation

## V1 Flow

```text
Job Description ─────┐
                     ├──> AI Analysis ──> Fit Score
Master Profile ──────┘                  ├─ Strong Matches
                                        ├─ Gaps
                                        ├─ Application Recommendations
                                        └─ Interview Questions
```

## Design Principles

- Never invent experience, skills, or achievements.
- Clearly distinguish evidence from inference.
- Keep the user in control; no automatic job submission.
- Start with a simple LLM workflow before adding RAG or agents.
- Keep personal profile data local/configurable where practical.
- Make AI output structured so it can be evaluated and displayed consistently.

## Learning Path

V1 starts with:

- LLM API integration
- Prompt design
- Structured JSON output
- Requirement extraction
- Evidence-based matching
- AI reliability and hallucination handling

Later versions will add:

- Embeddings and semantic search
- RAG over the Master Profile
- Tool/function calling
- Agent workflows
- Evaluation datasets and metrics
- Security, privacy, cost, latency, and monitoring

## Proposed V1 Components

```text
Frontend
  ├── JD Input
  ├── Profile Input
  └── Analysis Dashboard

Backend
  ├── Input validation
  ├── Job requirement extraction
  ├── Profile evidence extraction
  ├── Match/recommendation engine
  └── Structured response validation

LLM Provider
  └── Model API
```

## V1 Output Contract

The AI response should contain:

- overall_fit_score
- strong_matches[]
- partial_matches[]
- gaps[]
- application_recommendations[]
- interview_focus_areas[]
- evidence_used[]
- confidence_notes[]

## Explicitly Out of Scope for V1

- Auto-apply
- Browser automation
- Job scraping
- Agentic workflows
- Vector database
- Fine-tuning
- Authentication
- Persistent database

These will only be introduced when they solve a real product problem.
