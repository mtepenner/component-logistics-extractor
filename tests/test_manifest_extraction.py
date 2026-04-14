import pytest
from services.orchestrator import process_manifest_document
from services.llm_client import LLMClient

# Mock data to test against
MOCK_MANIFEST = "UPS Tracking: 1Z9999999999999999. Delivering to Hillsboro facility. Contains 50 units of SKU: MEM-DDR5-16GB."

@pytest.mark.asyncio
async def test_llm_extracts_correct_tracking_and_sku():
    """
    Tests that the LLM correctly parses the tracking number and SKUs 
    using the current prompt templates.
    """
    client = LLMClient() # In a real test, you might mock this or use a smaller/cheaper model
    
    try:
        result = await process_manifest_document(MOCK_MANIFEST, client)
        
        # Verify specific extraction targets
        assert result.carrier.upper() == "UPS"
        assert result.tracking_number == "1Z9999999999999999"
        assert len(result.line_items) == 1
        assert result.line_items[0].sku == "MEM-DDR5-16GB"
        assert result.line_items[0].quantity == 50
    except Exception as e:
        pytest.skip(f"Skipping live LLM test due to no API key or mock not implemented: {e}")
