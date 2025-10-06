from dotenv import load_dotenv
load_dotenv()

#Step1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List


class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


#Step2: Setup AI Agent from FrontEnd Request
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from ai_agent import get_response_from_ai_agent
import traceback

ALLOWED_MODELS = {
    "Groq": ["llama3-70b-8192", "llama-3.1-8b-instant", "llama-3.3-70b-versatile"],
    "OpenAI": ["gpt-5-mini"]
}

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState): 
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    try:
        # Validate provider
        if request.model_provider not in ALLOWED_MODELS:
            raise HTTPException(status_code=400, detail=f"Invalid provider: {request.model_provider}")
        
        # Validate model name for the given provider
        if request.model_name not in ALLOWED_MODELS[request.model_provider]:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid model name '{request.model_name}' for provider '{request.model_provider}'"
            )
        
        # Validate messages
        if not request.messages or not request.messages[0].strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        llm_id = request.model_name
        query = request.messages
        allow_search = request.allow_search
        system_prompt = request.system_prompt if request.system_prompt else "Act as an AI chatbot who is smart and friendly"
        provider = request.model_provider

        # Create AI Agent and get response from it! 
        response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
        
        # Return response as JSON
        return JSONResponse(content={"response": response})
    
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error in chat_endpoint: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

#Step3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
