# Product Requirements Document (PRD)
## AI Career Copilot — MVP

**Version:** 1.1  
**Status:** MVP Definition

## 1. Product Goal

Provide a simple AI-assisted workflow that analyzes a job description against a candidate profile and produces an explainable fit assessment, application recommendations, and interview preparation areas.

The repository itself must also function as a self-sufficient learning and product reference for the AI TPM concepts demonstrated by the project.

## 2. User Journey

```text
Enter Job Description
        ↓
Enter Candidate Profile
        ↓
Analyze Job
        ↓
Review Fit Score
        ↓
Review Matches & Gaps
        ↓
Review Application Recommendations
        ↓
Review Interview Focus Areas
```

## 3. MVP Features

### F1 — Job Description Input

User can paste a job description into the application.

**Acceptance criteria**
- User can enter a multi-line job description.
- Empty input is rejected with a clear message.
- The original JD is not modified before analysis.

### F2 — Candidate Profile Input

User can provide a candidate profile for comparison.

**Acceptance criteria**
- User can enter a multi-line profile.
- Empty profile is rejected.
- The public demo will use synthetic candidate information.
- Personal data is not committed to the public repository.

### F3 — Requirement Extraction

The system identifies major requirements from the JD, including skills, experience, responsibilities, domain knowledge, and preferred qualifications where identifiable.

**Acceptance criteria**
- Requirements are returned in structured categories.
- Important requirements are distinguishable from lower-priority preferences.
- The system avoids treating every keyword as equally important.

### F4 — Job Fit Assessment

The system compares extracted requirements with evidence in the candidate profile.

**Output**
- Overall fit score/rating.
- Strong matches.
- Partial matches.
- Gaps.
- Evidence supporting each major conclusion.

**Acceptance criteria**
- Every match or gap should reference available profile evidence or explicitly state that evidence is missing.
- Unsupported qualifications must not be presented as facts.
- The score must include a short explanation rather than appearing as unexplained precision.

### F5 — Application Recommendations

The system provides actionable recommendations for presenting the candidate's existing experience.

Recommendation categories:
- **Keep:** relevant evidence is already clear.
- **Strengthen:** relevant evidence exists but should be made more prominent or specific.
- **Gap:** the JD asks for capability for which the profile contains insufficient evidence.

**Acceptance criteria**
- Recommendations must be grounded in the profile and JD.
- The system must never recommend inventing experience.
- Recommendations should be concise and actionable.

### F6 — Interview Preparation

The system identifies likely interview focus areas based on the role and profile gaps.

**Acceptance criteria**
- Questions should be role-specific.
- Preparation areas should prioritize meaningful requirements and identified gaps.
- Questions should not assume experience that is absent from the profile.

### F7 — Learning & Knowledge Documentation

The project shall document the concepts learned while implementing the product.

Each major concept should, where applicable, cover:
- Plain-language definition.
- Why the concept matters.
- Where it appears in this project.
- Practical implementation example.
- Limitations/trade-offs.
- Failure or debugging experience.
- AI TPM takeaway/interview relevance.

Examples include LLMs, prompting, structured outputs, schema validation, hallucination, evaluation, embeddings, RAG, tool calling, agents, guardrails, security, cost, latency, and observability.

### F8 — Decision & Experiment Documentation

Important architecture decisions, implementation experiments, failures, fixes, and lessons learned shall be documented in the repository.

The documentation must allow a reader to understand the project without access to the original development conversation.

## 4. AI Output Contract

The backend should request and validate a structured response containing:

```json
{
  "overall_fit_score": 0,
  "fit_summary": "",
  "strong_matches": [],
  "partial_matches": [],
  "gaps": [],
  "application_recommendations": [],
  "interview_focus_areas": [],
  "evidence_used": [],
  "confidence_notes": []
}
```

The exact schema may evolve during implementation.

## 5. UX Requirements

- Single-page, simple workflow.
- Clear separation between inputs and AI results.
- Results should be scannable using cards/sections.
- Avoid excessive AI-generated text.
- Clearly distinguish evidence, recommendation, and uncertainty.
- Show errors in plain language.

## 6. Non-Functional Requirements

### Reliability
- Validate model responses before displaying them.
- Handle malformed or incomplete AI responses gracefully.

### Security & Privacy
- No secrets in source control.
- API keys must be supplied through environment variables.
- No personal candidate data in public repository files.
- No confidential employer data required.

### Maintainability
- Separate UI, API, AI orchestration, schemas, and configuration.
- Keep prompts version-controlled and reviewable.
- Use typed/validated structured outputs where practical.
- Keep documentation aligned with implementation changes.

### Cost
- Minimize unnecessary model calls.
- Keep prompts concise.
- Design the architecture so the model can be changed later.

### Performance
- Provide a clear loading state during analysis.
- Avoid unnecessary repeated LLM calls in MVP.

## 7. MVP Technical Approach

Initial implementation should use a straightforward LLM workflow rather than RAG or agents.

```text
Frontend
   ↓
Backend API
   ↓
Input Validation
   ↓
LLM Prompt + JD + Profile
   ↓
Structured JSON Response
   ↓
Response Validation
   ↓
Frontend Results
```

## 8. Explicitly Deferred Features

- RAG and vector database.
- Embedding-based profile retrieval.
- Agentic workflows.
- Browser automation.
- Job-board integrations.
- Automatic application submission.
- Persistent user accounts.
- Advanced evaluation infrastructure.

These will be introduced only when there is a clear product or learning reason.

## 9. Initial Test Scenarios

The MVP should be tested using multiple synthetic profiles and public-style sample JDs representing different technology/program roles.

At minimum:

1. Strong match.
2. Moderate/partial match.
3. Poor match.
4. JD with ambiguous requirements.
5. JD containing requirements absent from the profile.

## 10. Definition of Done — MVP

The MVP is complete when a user can:

1. Enter a JD.
2. Enter a candidate profile.
3. Run analysis.
4. Receive validated structured output.
5. Understand why the candidate matches or does not match.
6. Receive evidence-based application recommendations.
7. Receive targeted interview preparation areas.
8. Follow the repository documentation to understand the product, implementation, key AI concepts, and major lessons learned.

No automatic application submission is part of MVP.
