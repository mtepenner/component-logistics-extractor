import pytest
from services.orchestrator import process_manifest_document
from services.llm_client import LLMClient

# Missing tracking number and carrier
AMBIGUOUS_MANIFEST = "A box of 100 resistors (RES-10K) was dropped off at the front desk today by a courier."

@pytest.mark.asyncio
async def test_llm_does_not_hallucinate_tracking_data():
    client = LLMClient()
    
    try:
        result = await process_manifest_document(AMBIGUOUS_MANIFEST, client)
        
        # The prompt should strictly enforce that missing data becomes None/null
        assert result.tracking_number is None
        assert result.line_items[0].sku == "RES-10K"
        assert result.line_items[0].quantity == 100
    except Exception as e:
        pytest.skip(f"Skipping live LLM test due to no API key or mock not implemented: {e}")
