from dotenv import load_dotenv
load_dotenv()

#Step1: Setup API Keys for Groq, OpenAI and Tavily
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm=ChatOpenAI(model="gpt-5-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)

#Step3: Setup AI Agent with Search tool functionality
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    try:
        if provider == "Groq":
            llm = ChatGroq(model=llm_id, temperature=0.7)
        elif provider == "OpenAI":
            llm = ChatOpenAI(model=llm_id, temperature=0.7)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

        tools = [TavilySearchResults(max_results=2)] if allow_search else []
        
        # Create the agent
        agent = create_react_agent(
            model=llm,
            tools=tools
        )
        
        # Handle query properly - it's a list from the backend
        user_message = query[0] if isinstance(query, list) else query
        
        # Build messages with proper system prompt handling
        messages = []
        if system_prompt and system_prompt.strip():
            messages.append(SystemMessage(content=system_prompt))
        messages.append(HumanMessage(content=user_message))
        
        state = {"messages": messages}
        
        # Invoke the agent
        response = agent.invoke(state)
        
        # Extract the final AI response
        final_messages = response.get("messages", [])
        ai_messages = [message.content for message in final_messages if isinstance(message, AIMessage)]
        
        if ai_messages:
            return ai_messages[-1]
        else:
            return "I apologize, but I couldn't generate a response. Please try again."
            
    except Exception as e:
        print(f"Error in get_response_from_ai_agent: {str(e)}")
        return f"Error generating response: {str(e)}"
