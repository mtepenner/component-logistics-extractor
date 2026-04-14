from typing import Optional
from pydantic import Field
from .base import ExtractorBaseModel

class Component(ExtractorBaseModel):
    """Schema for an individual hardware component."""
    
    sku: str = Field(
        ..., 
        description="The exact alphanumeric stock keeping unit. If missing, extract the manufacturer part number."
    )
    name: str = Field(
        ..., 
        description="The common name of the part, e.g., 'OptiTrack Motion Sensor' or 'Silicon Wafer 300mm'."
    )
    quantity: int = Field(
        ..., 
        description="The number of units. Must be an integer. If the text says 'a dozen', output 12."
    )
    location_bin: Optional[str] = Field(
        None, 
        description="The warehouse bin or aisle location if mentioned, e.g., 'Aisle 4, Bin B'."
    )

class InventoryUpdate(ExtractorBaseModel):
    """Schema for extracting a batch of inventory changes."""
    
    vendor_name: str = Field(..., description="The name of the company supplying the components.")
    components: list[Component] = Field(..., description="List of all parts mentioned in the document.")
    requires_follow_up: bool = Field(
        ..., 
        description="True if the text mentions backorders, missing items, or delays. False otherwise."
    )
