import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import os
from dotenv import load_dotenv
from langchain_core.tools import Tool
from langchain_google_community import GoogleSearchAPIWrapper

load_dotenv()

os.environ["GOOGLE_CSE_ID"] = os.getenv("GOOGLE_CSE_ID")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

search = GoogleSearchAPIWrapper()

googleSearchTool = Tool(
    name="Google Research Search",
    description="Search for reliable, up-to-date academic and research information on the web using Google's API.",
    func=search.run,
)

# Arxiv and Wikipedia Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxivTool = ArxivQueryRun(api_wrapper=arxiv_wrapper)
arxivTool.description = "Query academic papers from arXiv for in-depth scholarly insights."

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wikiTool = WikipediaQueryRun(api_wrapper=api_wrapper)
wikiTool.description = "Fetch summarized and detailed information from Wikipedia to support deep research."

duckduckgoSearchTool = DuckDuckGoSearchRun(
    name="DuckDuckGo Broad Search", 
    description="Perform a broad web search to gather diverse perspectives and additional insights for research."
)

st.title("🔎 LangChain - Deep Research Assistant")

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

if api_key:

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": (
                    "You are a  deep research assistant. You can conduct thorough research "
                    "across academic sources, news, and the web. Provide a Research Repost of User Query"
                ),
            }
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder="Enter your deep research query here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1, api_key=api_key)
        tools = [googleSearchTool, duckduckgoSearchTool, arxivTool, wikiTool]

        search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({'role': 'assistant', "content": response})
            st.write(response)
else:
    st.warning("⚠️ Please enter your Gemini API Key to use the application")
