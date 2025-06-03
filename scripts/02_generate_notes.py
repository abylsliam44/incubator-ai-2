import json
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field

load_dotenv()
client = OpenAI()

class Note(BaseModel):
    id: int = Field(..., ge=1, le=10)
    heading: str
    summary: str = Field(..., max_length=150)
    page_ref: int | None = None

system_prompt = (
    "You are a study summarizer. Return exactly 10 unique notes that will help prepare for the exam. "
    "Respond only with valid JSON matching the Note[] schema."
)

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": system_prompt}],
    response_format={"type": "json_object"}
)

notes = [Note(**n) for n in json.loads(resp.choices[0].message.content)["notes"]]
json.dump([n.model_dump() for n in notes], open("exam_notes.json", "w"), indent=2)
print("NOTES CREATED")
