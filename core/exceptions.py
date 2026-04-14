from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

class LLMOutputParsingError(Exception):
    """
    Raised when the LLM returns an output that cannot be 
    validated against our strict Pydantic schemas.
    """
    def __init__(self, message: str, raw_output: str = None):
        self.message = message
        self.raw_output = raw_output
        super().__init__(self.message)

class DocumentProcessingError(Exception):
    """Raised when OCR or text extraction from a file fails."""
    pass

class PromptTemplateError(Exception):
    """Raised if a required YAML prompt template is missing or malformed."""
    pass


# --- FastAPI Global Exception Handlers ---

async def llm_parsing_exception_handler(request: Request, exc: LLMOutputParsingError):
    """Intercepts LLM parsing errors and returns a clean 422 Unprocessable Entity."""
    logger.error(f"LLM Parsing Failed: {exc.message}. Raw: {exc.raw_output}")
    return JSONResponse(
        status_code=422,
        content={
            "error": "LLM_PARSING_FAILED",
            "message": "The AI model returned data that did not match the strict JSON schema.",
            "details": exc.message
        },
    )

async def document_processing_exception_handler(request: Request, exc: DocumentProcessingError):
    """Intercepts file reading/OCR errors and returns a 400 Bad Request."""
    logger.error(f"Document processing failed: {str(exc)}")
    return JSONResponse(
        status_code=400,
        content={
            "error": "DOCUMENT_PROCESSING_FAILED",
            "message": "Failed to read or extract text from the provided file.",
            "details": str(exc)
        },
    )
