Study-Assistant Lab is a tiny demo that shows how to talk to the OpenAI Assistants API from plain Python scripts.  

* Put any PDFs you want to study in **data/**.  
* Create a virtual-env, run `pip install -r requirements.txt`, drop your paid `OPENAI_API_KEY` in a local `.env` (never commit it).  
* Run `python scripts/00_bootstrap.py` – this uploads the PDFs and builds an assistant.  
* Ask it questions with `python scripts/01_qna_assistant.py "your question"` and it replies using passages from your files.  
* Need quick revision notes? `python scripts/02_generate_notes.py` writes ten bite-sized notes to `exam_notes.json`.

`.env` and `venv/` are already ignored, so secrets stay local. If you ever push a key by mistake, wipe it from history and generate a new one in the OpenAI dashboard.
