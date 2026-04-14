import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

from core.config import settings
from core.exceptions import (
    LLMOutputParsingError, 
    DocumentProcessingError,
    llm_parsing_exception_handler,
    document_processing_exception_handler
)
from api.routes import api_router

# Set up basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Initialize the FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="An AI-powered extraction API for supply chain and logistics text.",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Register Custom Global Exception Handlers
app.add_exception_handler(LLMOutputParsingError, llm_parsing_exception_handler)
app.add_exception_handler(DocumentProcessingError, document_processing_exception_handler)

# Include the main API router (which contains /manifests, /qc-reports, etc.)
app.include_router(api_router)

@app.get("/", include_in_schema=False)
async def root():
    """Redirects the root URL to the interactive Swagger UI documentation."""
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["System"])
async def health_check():
    """Basic health check endpoint."""
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "version": settings.VERSION
    }

if __name__ == "__main__":
    # This allows you to run the app directly using `python main.py`
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=(settings.ENVIRONMENT == "development")
    )
