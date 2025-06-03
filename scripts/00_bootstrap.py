import os, glob, json, time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

pdf_paths = glob.glob(os.path.join("data", "*.pdf"))
file_ids = [
    client.files.create(purpose="assistants", file=open(p, "rb")).id
    for p in pdf_paths
]

vector_store = client.beta.vector_stores.create_and_poll(
    name="study_vs",
    file_ids=file_ids,                 
)

assistant = client.beta.assistants.create(
    name="Study Q&A Assistant",
    instructions="You are a helpful tutor. Use the attached files to answer questions and cite sources.",
    model="gpt-4o-mini",
    tools=[{"type": "file_search"}],
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

json.dump(
    {
        "assistant_id": assistant.id,
        "vector_store_id": vector_store.id,
        "file_ids": file_ids,
    },
    open("bootstrap_output.json", "w"),
    indent=2,
)

print("✅ BOOTSTRAP DONE")
print("assistant_id   :", assistant.id)
print("vector_store_id:", vector_store.id)
print("file_ids       :", file_ids)
