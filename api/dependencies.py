from fastapi import Header, HTTPException, status
import os

# In a real app, this would be loaded from core/config.py
API_KEY = os.getenv("EXTRACTOR_API_KEY", "dev-secret-key")

async def verify_api_key(x_api_key: str = Header(...)):
    """
    Dependency to enforce API key authentication on protected routes.
    """
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key provided.",
        )
    return x_api_key

# Placeholder for LLM service dependency
async def get_llm_service():
    """
    Dependency to inject the LLM client (e.g., Gemini API wrapper).
    Allows for easy mocking during unit testing.
    """
    # from services.llm_client import LLMClient
    # return LLMClient()
    pass
