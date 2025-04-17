# agent-agno

LANCIA QUESTI 5 COMANDI NEL TERMINALE

python3.12 -m venv .venv
source .venv/bin/activate
pip install -U agno anthropic
export ANTHROPIC_API_KEY=sk-
python basic_agent.py

---

pip install -U duckduckgo-search openai agno
export OPENAI_API_KEY=xxx
python agent_with_tool.py

---

pip install openai duckduckgo-search newspaper4k lxml_html_clean agno
python researcher_with_expected_output.py