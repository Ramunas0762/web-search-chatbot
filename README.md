# web-search-chatbot

Here's a README.md file tailored for your OpenAI Agent Chatbot Streamlit app:

# 🤖 OpenAI Agent Chatbot

This is a simple chatbot web app built with [Streamlit](https://streamlit.io) and powered by the [OpenAI Agents SDK](https://github.com/openai/openai-python/tree/main/openai/agents). The agent is equipped with a built-in `WebSearchTool`, enabling it to answer user queries using live web search when necessary.

## ✨ Features

- Interactive chatbot UI using Streamlit
- Uses OpenAI Agents SDK for intelligent responses
- Integrates the `WebSearchTool` for up-to-date web information
- Asynchronous handling of agent responses

## 🛠️ Requirements

- Python 3.8+
- OpenAI Python SDK (with Agents support)
- Streamlit

## 📦 Installation

1. Clone the repository or copy the code.

2. Install dependencies:

```bash
pip install streamlit openai
Note: Ensure you have access to the openai.agents module (requires access to OpenAI's Agents SDK).

3. Set your OpenAI API key as an environment variable:

bash
Copy
Edit
export OPENAI_API_KEY="your-api-key-here"
🚀 Usage
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
(Assuming your file is named app.py.)

Then, navigate to http://localhost:8501 in your browser.

🧠 Agent Instructions
The chatbot is initialized with the following instructions:

"You are a helpful assistant. Use the web_search tool if you do not know the answer."

This ensures the agent uses the web intelligently when it lacks internal knowledge.

🧪 Example
User input:

vbnet
Copy
Edit
What's the latest news on artificial intelligence regulation?
Bot response:

sql
Copy
Edit
(OpenAI Agent performs web search and returns a summarized response.)
📁 File Structure
bash
Copy
Edit
.
├── app.py             # Main Streamlit app
├── agents.py          # Defines Agent, WebSearchTool, and Runner
└── README.md          # This file
📄 License
This project is licensed under the MIT License. See LICENSE for details.

Built with ❤️ using Streamlit and OpenAI