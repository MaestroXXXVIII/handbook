from fastapi import FastAPI

from .health_check import router
from .organization import organization_router


def init_routes(app: FastAPI) -> None:
    prefix: str = '/api/v1'
    app.include_router(
        router=router,
        prefix=f'{prefix}/health-check',
        tags=['Test'],
    )
    app.include_router(
        router=organization_router,
        prefix=f'{prefix}/organizations',
        tags=['Organization'],
    )


__all__ = ('init_routes',)
