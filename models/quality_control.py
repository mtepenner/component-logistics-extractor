from enum import Enum
from pydantic import Field
from .base import ExtractorBaseModel

class DefectCategory(str, Enum):
    COSMETIC = "cosmetic"
    ELECTRICAL = "electrical"
    MECHANICAL = "mechanical"
    MISSING_PART = "missing_part"
    UNKNOWN = "unknown"

class QCResult(ExtractorBaseModel):
    """Schema for a single component's quality check."""
    
    component_id: str = Field(..., description="The ID or serial number of the inspected part.")
    passed_inspection: bool = Field(..., description="True if the part is good to use, False if defective.")
    defect_category: DefectCategory = Field(
        ..., 
        description="Categorize the defect. If the part passed, use 'unknown'."
    )
    severity: int = Field(
        ..., 
        ge=1, le=5, 
        description="Rate the defect severity from 1 (minor scratch) to 5 (complete critical failure). Use 1 if it passed."
    )
    inspector_notes_summary: str = Field(
        ..., 
        description="A concise, 1-sentence summary of the inspector's original notes."
    )

class QCReportExtraction(ExtractorBaseModel):
    """Schema for extracting data from a full batch QC report."""
    
    batch_number: str = Field(..., description="The overarching batch or lot number.")
    inspection_date: str = Field(..., description="Date of the inspection in YYYY-MM-DD format.")
    results: list[QCResult] = Field(..., description="The individual results for each part inspected.")
