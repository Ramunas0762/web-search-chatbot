import streamlit as st
from agents import Agent, WebSearchTool, Runner
import asyncio

st.set_page_config(page_title="OpenAI Agent Chatbot", page_icon="🤖")
st.title("🤖 OpenAI Agent Chatbot")

st.markdown("""
This chatbot uses the OpenAI Agents Python SDK and includes the built-in WebSearchTool for web search.
""")

# Create an agent with the built-in WebSearchTool
agent = Agent(
    name="OpenAI Assistant",
    tools=[WebSearchTool()],
    instructions="You are a helpful assistant. Use the web_search tool if you do not know the answer."
)

async def get_agent_response(message):
    result = await Runner.run(agent, message)
    return result.final_output

with st.form("chat_form"):
    user_message = st.text_input("Your message", "")
    submitted = st.form_submit_button("Send")

if submitted and user_message.strip():
    with st.spinner("OpenAI Agent is thinking..."):
        answer = asyncio.run(get_agent_response(user_message))
    st.markdown(f"**Bot:** {answer}")