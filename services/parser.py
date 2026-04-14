import json
from pydantic import BaseModel, ValidationError
from core.exceptions import LLMOutputParsingError

def validate_and_parse_llm_output(raw_output: dict | str, model_class: type[BaseModel]) -> BaseModel:
    """
    Attempts to validate the raw LLM output against the target Pydantic model.
    Raises a custom LLMOutputParsingError if validation fails.
    """
    try:
        # If the output is a string, parse it to a dict first
        if isinstance(raw_output, str):
            raw_output = json.loads(raw_output)
            
        # Validate against the Pydantic model
        validated_data = model_class.model_validate(raw_output)
        return validated_data

    except ValidationError as e:
        # The LLM hallucinated a key, used the wrong type, or violated an Enum
        raise LLMOutputParsingError(
            message=f"LLM output failed Pydantic validation: {e.errors()}",
            raw_output=str(raw_output)
        )
    except json.JSONDecodeError as e:
        raise LLMOutputParsingError(
            message=f"LLM returned malformed JSON: {str(e)}",
            raw_output=str(raw_output)
        )
