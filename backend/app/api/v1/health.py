from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Healthcheck")
def healthcheck() -> dict[str, str]:
    """Simple liveness probe endpoint."""
    return {
        "status": "ok",
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
    }
