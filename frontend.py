from dotenv import load_dotenv
load_dotenv()

# Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st

st.set_page_config(
    page_title="AI Chatbot Agents - Bhupesh Danewa", 
    layout="centered",
    page_icon="🤖"
)

# Header with personal branding
st.title("🤖 AI Chatbot Agents")
st.markdown("### Created by **Bhupesh Danewa**")
st.markdown("**MTech AI, MANIT** | *Artificial Intelligence Enthusiast*")

# Social links
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/bhupesh-danewa)")
with col2:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bhupesh-danewa)")

st.markdown("---")
st.write("**Create and Interact with AI Agents powered by multiple LLM providers!**")

# Sidebar for better organization
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Model provider selection
    provider = st.radio("Select Provider:", ("Groq", "OpenAI"))
    
    MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mistral-saba-24b"]
    MODEL_NAMES_OPENAI = ["gpt-4o-mini"]
    
    if provider == "Groq":
        selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
    elif provider == "OpenAI":
        selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)
    
    allow_web_search = st.checkbox("🌐 Allow Web Search")
    
    st.markdown("---")
    st.markdown("### 📊 Model Info")
    if provider == "Groq":
        st.info("**Groq**: Ultra-fast inference with specialized hardware")
    else:
        st.info("**OpenAI**: Advanced reasoning capabilities")

# Main interface
system_prompt = st.text_area(
    "🎯 Define your AI Agent:", 
    height=100, 
    placeholder="Enter a system prompt to define your AI agent's role and behavior...",
    help="This defines how your AI agent will behave and respond to queries."
)

user_query = st.text_area(
    "💬 Enter your query:", 
    height=150, 
    placeholder="Ask anything! Your AI agent is ready to help...",
    help="Type your question or request here."
)

API_URL = "http://127.0.0.1:9999/chat"

# Enhanced button with loading state
if st.button("🚀 Ask Agent!", type="primary", use_container_width=True):
    if user_query.strip():
        # Step2: Connect with backend via URL
        import requests
        
        with st.spinner('🤔 Agent is thinking...'):
            payload = {
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_web_search
            }
            
            try:
                response = requests.post(API_URL, json=payload, timeout=30)
                if response.status_code == 200:
                    response_data = response.json()
                    if "error" in response_data:
                        st.error(f"❌ Error: {response_data['error']}")
                    else:
                        st.success("✅ Response generated successfully!")
                        st.subheader("🤖 Agent Response")
                        
                        # Better response formatting
                        with st.container():
                            st.markdown("**Final Response:**")
                            st.markdown(f"{response_data}")
                            
                        # Model info display
                        with st.expander("ℹ️ Response Details"):
                            st.write(f"**Model Used:** {selected_model}")
                            st.write(f"**Provider:** {provider}")
                            st.write(f"**Web Search Enabled:** {'Yes' if allow_web_search else 'No'}")
                else:
                    st.error(f"❌ API Error: Status code {response.status_code}")
                    
            except requests.exceptions.Timeout:
                st.error("⏰ Request timed out. Please try again.")
            except requests.exceptions.ConnectionError:
                st.error("🔌 Connection error. Please ensure the backend server is running.")
            except Exception as e:
                st.error(f"❌ Unexpected error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a query before asking the agent!")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.8em;'>
        <p>Built with ❤️ by Bhupesh Danewa | MTech AI, MANIT</p>
        <p>Powered by Streamlit & LangGraph</p>
    </div>
    """, 
    unsafe_allow_html=True
)