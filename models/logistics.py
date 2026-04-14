from typing import Optional
from datetime import date
from pydantic import Field
from .base import ExtractorBaseModel
from .inventory import Component

class ManifestExtraction(ExtractorBaseModel):
    """Schema for parsing unstructured shipping manifests and delivery receipts."""
    
    carrier: str = Field(
        ..., 
        description="The shipping company, e.g., FedEx, UPS, DHL, or a local freight line."
    )
    tracking_number: str = Field(
        ..., 
        description="The primary tracking or waybill number. Leave null if not explicitly stated."
    )
    ship_date: Optional[date] = Field(
        None, 
        description="The date the package was shipped. Format as YYYY-MM-DD."
    )
    estimated_delivery: Optional[date] = Field(
        None, 
        description="The estimated date of arrival. Format as YYYY-MM-DD."
    )
    sender_facility: Optional[str] = Field(
        None,
        description="The origin facility or city, e.g., 'Toronto, ON' or 'Hillsboro Distribution Center'."
    )
    line_items: list[Component] = Field(
        ..., 
        description="The list of components contained in this shipment."
    )
