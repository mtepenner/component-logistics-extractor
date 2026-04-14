from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ExtractorBaseModel(BaseModel):
    """
    Base configuration for all extraction models.
    """
    model_config = ConfigDict(
        populate_by_name=True,
        str_strip_whitespace=True,
        extra="ignore" # Ignore hallucinated keys from the LLM
    )
