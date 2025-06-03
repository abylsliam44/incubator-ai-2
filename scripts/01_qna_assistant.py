import json, sys, time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

assistant_id = json.load(open("bootstrap_output.json"))["assistant_id"]
thread = client.beta.threads.create()

q = " ".join(sys.argv[1:]) or "Explain the difference between definite and indefinite integrals."
client.beta.threads.messages.create(thread.id, role="user", content=q)
run = client.beta.threads.runs.create(thread.id, assistant_id=assistant_id)

while client.beta.threads.runs.retrieve(thread.id, run.id).status != "completed":
    time.sleep(0.5)

for m in client.beta.threads.messages.list(thread.id).data:
    if m.role == "assistant":
        print(m.content[0].text.value.strip())
