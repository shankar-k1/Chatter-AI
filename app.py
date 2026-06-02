# app.py
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# ── Page config ──────────────────────────────────────────
st.set_page_config(page_title="Local Chat", page_icon="🦙", layout="centered")
st.title("🦙 Local Chat — Llama 3.2")

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.header("Settings")

    model_name = st.selectbox(
        "Model",
        ["llama3.2", "llama3.2:1b", "mistral", "phi3"],
        index=0
    )

    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1,
        help="Higher = more creative. Lower = more focused.")

    system_prompt = st.text_area(
        "System prompt",
        value="You are a helpful assistant. Be concise and clear.",
        height=100
    )

    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption(f"Messages in session: {len(st.session_state.get('messages', []))}")

# ── Session state — this persists across reruns ───────────
# Streamlit reruns the whole script on every interaction
# session_state is how we keep data alive between reruns
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of {"role": "user"/"assistant", "content": "..."}

# ── Render existing chat history ──────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Chat input ────────────────────────────────────────────
if prompt := st.chat_input("Message Llama..."):

    # Show user message immediately
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build history for LangChain from session state
    history = [SystemMessage(content=system_prompt)]
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            history.append(HumanMessage(content=msg["content"]))
        else:
            history.append(AIMessage(content=msg["content"]))

    # Stream the response
    llm = ChatOllama(model=model_name, temperature=temperature)

    with st.chat_message("assistant"):
        response = st.write_stream(
            chunk.content for chunk in llm.stream(history)
        )

    # Save assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
