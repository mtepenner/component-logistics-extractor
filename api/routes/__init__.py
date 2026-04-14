from fastapi import APIRouter
from .manifests import router as manifests_router
from .vendor_emails import router as vendor_emails_router
from .qc_reports import router as qc_reports_router

# Create a master router for the API v1 namespace
api_router = APIRouter(prefix="/api/v1")

# Include all sub-routers
api_router.include_router(manifests_router)
api_router.include_router(vendor_emails_router)
api_router.include_router(qc_reports_router)
