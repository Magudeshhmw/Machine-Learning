import streamlit as st
from llama_cpp import Llama

# Set page config
st.set_page_config(page_title="Chat with Mistral LLM", layout="centered")

# Load the GGUF model (do this only once)
@st.cache_resource
def load_model():
    return Llama(
        model_path="models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
        n_ctx=2048,
        n_threads=8,
        use_mlock=True
    )

llm = load_model()

# Initialize session state
if "chat_started" not in st.session_state:
    st.session_state.chat_started = False
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🧠 Chat with HMW LLM Model")
st.markdown("Say **'hii'** to start chatting. Say **'thanks'** to end.")

# Input field
user_input = st.text_input("You:", key="input")

# On submit
if user_input:
    user_input_lower = user_input.strip().lower()

    if user_input_lower == "thanks":
        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Model", "You're welcome! Have a great day 😊"))
        st.session_state.chat_started = False
    elif user_input_lower == "hii":
        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Model", "Hello! Ask me anything."))
        st.session_state.chat_started = True
    elif not st.session_state.chat_started:
        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Model", "Please say 'hii' to start chatting."))
    else:
        # Normal inference
        prompt = f"### Instruction:\n{user_input}\n\n### Response:"
        output = llm(prompt, max_tokens=100, temperature=0.7, stop=["###"])
        response = output["choices"][0]["text"].strip()

        # Save messages
        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Model", response))

# Display chat history
for sender, message in st.session_state.messages:
    with st.chat_message("user" if sender == "You" else "assistant"):
        st.markdown(message)
