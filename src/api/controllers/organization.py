from typing import Annotated

from fastapi import APIRouter, Query, status, HTTPException, Depends, Path
from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute

from src.api.api_key import verify_api_key
from src.api.dtos import QueryParamDTO, OrganizationDTO
from src.features.organization.application.dtos import FilterParamDTO
from src.features.organization.application.interactors import (
    GetOrganizationByIdInteractor,
    GetOrganizationByTitleInteractor,
    GetOrganizationsInteractor
)
from src.features.organization.exceptions import OrganizationNotFoundError

organization_router = APIRouter(route_class=DishkaRoute)


@organization_router.get(
    '/',
    dependencies=[Depends(verify_api_key)],
    summary='Поиск организаций по заданным фильтрам.',
    description='Ищет организации по заданным фильтрам. Возвращает список организаций.'
)
async def get_organizations(
        query: Annotated[QueryParamDTO, Query()],
        interactor: FromDishka[GetOrganizationsInteractor]
) -> list[OrganizationDTO]:
    organizations = await interactor.execute(FilterParamDTO(**query.model_dump()))
    return [OrganizationDTO.model_validate(organization) for organization in organizations]


@organization_router.get(
    '/search',
    dependencies=[Depends(verify_api_key)],
    summary="Поиск организации по названию",
    description="Ищет организацию по её наименованию. Возвращает первую найденную организацию."
)
async def get_organization_by_title(
        organization_title: Annotated[str, Query(description='Наименование организации.')],
        interactor: FromDishka[GetOrganizationByTitleInteractor]
) -> OrganizationDTO:
    try:
        organization = await interactor.execute(organization_title)
    except OrganizationNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Организация с наименованием {organization_title} не найдена'
        )
    return OrganizationDTO.model_validate(organization)


@organization_router.get(
    '/{organization_id}',
    dependencies=[Depends(verify_api_key)],
    summary='Поиск организации по ее идентификатору.',
    description='Ищет организацию по её идентификатору'
)
async def get_organization_by_id(
        organization_id: Annotated[int, Path(description='Идентификатор организации.')],
        interactor: FromDishka[GetOrganizationByIdInteractor]
) -> OrganizationDTO:
    try:
        organization = await interactor.execute(organization_id)
    except OrganizationNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Организация с идентификатором {organization_id} не найдена'
        )
    return OrganizationDTO.model_validate(organization)
