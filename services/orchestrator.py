import yaml
from models.logistics import ManifestExtraction
from services.llm_client import LLMClient
from services.parser import validate_and_parse_llm_output
from core.exceptions import DocumentProcessingError

# Load prompt templates
with open("prompt_engineering/templates/extraction_prompts.yaml", "r") as f:
    PROMPTS = yaml.safe_load(f)

async def process_manifest_document(raw_text: str, llm_client: LLMClient) -> ManifestExtraction:
    """
    Orchestrates the extraction of a shipping manifest.
    """
    if not raw_text or len(raw_text.strip()) == 0:
        raise DocumentProcessingError("Provided document text is empty.")

    # 1. Construct the prompt
    template = PROMPTS["manifest_extraction"]["template"]
    formatted_prompt = template.format(raw_text=raw_text)

    # 2. Call the LLM with the prompt and the expected Pydantic schema
    raw_llm_response = await llm_client.generate_structured_output(
        prompt=formatted_prompt,
        schema=ManifestExtraction
    )

    # 3. Validate the output
    validated_manifest = validate_and_parse_llm_output(raw_llm_response, ManifestExtraction)
    
    return validated_manifest
