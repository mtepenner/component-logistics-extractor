from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    """
    Application configuration variables. 
    Pydantic automatically reads these from environment variables or a .env file.
    """
    PROJECT_NAME: str = "Component Logistics Extractor API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # API Security
    EXTRACTOR_API_KEY: str = "dev-secret-key"

    # LLM Configurations
    LLM_PROVIDER: str = "gemini"  # Default to Gemini, could switch to "openai"
    GEMINI_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None
    
    # Model selections
    EXTRACTION_MODEL: str = "gemini-1.5-pro"
    FALLBACK_MODEL: str = "gemini-1.5-flash"

    # Pydantic v2 configuration for loading the .env file
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )

# Instantiate a global settings object to be imported across the app
settings = Settings()
