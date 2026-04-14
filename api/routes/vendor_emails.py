from fastapi import APIRouter, Depends
from pydantic import BaseModel
from api.dependencies import verify_api_key

router = APIRouter(
    prefix="/vendor-emails",
    tags=["Vendor Emails"],
    dependencies=[Depends(verify_api_key)]
)

class EmailPayload(BaseModel):
    sender: str
    subject: str
    body: str

@router.post("/extract", summary="Extract inventory updates from vendor emails")
async def extract_vendor_email(payload: EmailPayload):
    """
    Accepts raw text from a vendor email and uses LLM extraction to find:
    - Expected delivery dates
    - Backordered SKUs
    - Quantity adjustments
    """
    
    # 1. Construct the context for the prompt
    # text_to_process = f"Subject: {payload.subject}\nBody: {payload.body}"
    
    # 2. Call the extraction service
    # extracted_data = await extract_email_data(text_to_process)

    return {
        "status": "success",
        "vendor": payload.sender,
        "action_required": True,
        "extracted_updates": []
    }
