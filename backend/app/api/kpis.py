"""KPI and metrics endpoints."""
from fastapi import APIRouter

router = APIRouter()

# async def get_kpis():
#     """Get all KPIs."""
#     return {"kpis": []}

@router.get("/kpis")
def get_kpis():
    """Get all KPIs. - harcoded for now."""
    return {
        "velocity": 38,
        "throughput": 54,
        "blocked_percentage": 12.5
    }

@router.get("/kpis/{kpi_id}")
async def get_kpi(kpi_id: int):
    """Get a specific KPI."""
    return {"id": kpi_id}


@router.post("/kpis/calculate")
async def calculate_kpis(data: dict):
    """Calculate KPIs from data."""
    return {"results": {}}
