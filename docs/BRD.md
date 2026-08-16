# Business Requirements Document (BRD)
## AI Career Copilot

**Version:** 1.0  
**Status:** MVP Definition

## 1. Business Problem

Job seekers spend significant time manually comparing job descriptions with their experience, deciding what to emphasize in an application, and preparing for interviews. The process is repetitive, inconsistent, and often relies on keyword matching rather than evidence-based assessment.

The AI Career Copilot will provide structured decision support that helps a user understand how well a candidate profile aligns with a job opportunity and what should be emphasized during the application process.

## 2. Product Vision

Create an AI-assisted career decision-support tool that turns an unstructured job description and a candidate profile into clear, evidence-based recommendations while keeping the candidate in control.

## 3. Business Objectives

- Reduce time spent manually analyzing job descriptions.
- Improve consistency of job-fit assessment.
- Help users identify relevant experience that should be emphasized.
- Identify genuine capability gaps without fabricating qualifications.
- Improve interview preparation based on the target role.
- Provide a practical platform for demonstrating responsible AI product delivery.

## 4. Target Users

Primary user:
- Professionals evaluating and applying for technology, project/program management, product, and related roles.

The public project will use generic/synthetic candidate data. Personal candidate information will remain outside the public repository.

## 5. MVP Scope

### In Scope

- Job description input.
- Candidate profile input.
- Requirement extraction.
- Job-fit assessment.
- Strong-match identification.
- Partial-match identification.
- Gap identification.
- Application recommendations.
- Interview preparation areas.
- Structured AI output.

### Out of Scope

- Automatic job applications or submissions.
- Browser automation.
- Job-board scraping.
- Persistent personal-data storage.
- Fine-tuning models.
- Autonomous agents.
- Enterprise integrations.
- Automated hiring decisions.

## 6. Key Business Requirements

| ID | Requirement |
|---|---|
| BR-01 | The system shall analyze a supplied job description. |
| BR-02 | The system shall compare job requirements with a candidate profile. |
| BR-03 | The system shall distinguish strong matches, partial matches, and gaps. |
| BR-04 | Recommendations shall be based on evidence available in the candidate profile. |
| BR-05 | The system shall not invent experience, skills, certifications, or achievements. |
| BR-06 | The system shall provide actionable application recommendations. |
| BR-07 | The system shall identify interview preparation areas relevant to the role. |
| BR-08 | AI results shall be returned in a consistent structured format. |

## 7. Success Measures

Initial MVP success will be measured by:

- Users can complete an analysis from JD input to recommendations in one workflow.
- Results are understandable and actionable.
- Recommendations can be traced to evidence in the candidate profile.
- The system avoids unsupported claims.
- Test cases produce consistent structured output.
- The application demonstrates a clear AI product workflow suitable for portfolio and AI TPM learning.

## 8. Constraints & Assumptions

- The product must work without access to employer or confidential enterprise data.
- Public repository content must not expose personal job-search information.
- Synthetic/public test data will be used for demonstrations.
- The initial version should remain simple enough to understand and modify while learning AI concepts.
- The human user remains the final decision maker.

## 9. Risks

- LLM hallucination may produce unsupported recommendations.
- Job descriptions may be ambiguous or incomplete.
- Candidate profiles may contain insufficient evidence.
- Fit scores may create false precision if presented without explanation.
- LLM cost and latency may increase as workflows become more complex.

## 10. Future Direction

After the MVP, the product may evolve toward semantic profile retrieval, RAG, tool calling, agentic workflows, evaluation frameworks, application tracking, and production-grade security and observability.
