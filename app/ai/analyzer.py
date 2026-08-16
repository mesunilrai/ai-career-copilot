import json
import os
from pathlib import Path

from groq import Groq


PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "job_analysis.txt"


def analyze_job(job_description: str, candidate_profile: str) -> dict:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not configured")

    prompt_template = PROMPT_PATH.read_text(encoding="utf-8")
    prompt = prompt_template.format(
        job_description=job_description,
        candidate_profile=candidate_profile,
    )

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format={"type": "json_object"},
    )

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("The AI provider returned an empty response")

    try:
        return json.loads(content)
    except json.JSONDecodeError as exc:
        raise RuntimeError("The AI provider returned invalid JSON") from exc
