from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.features.organization.application.dtos import FilterParamDTO
from src.features.organization.domain.repository import IOrganizationRepository
from src.features.organization.domain.entities.organization import Organization
from .models import OrganizationModel, BuildingModel, ActivityModel
from src.infrastructure.mapper import OrganizationMapper


class OrganizationRepository(IOrganizationRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session


    async def _build_organization_filters(self, filter_params: FilterParamDTO) -> list:
        filters = []

        if filter_params:
            if filter_params.building_address:
                filters.append(BuildingModel.address.ilike(f'%{filter_params.building_address}%'))

            if filter_params.activity_title:
                activity_ids = await self._get_activity_descendant_ids(filter_params.activity_title)
                if activity_ids:
                    filters.append(OrganizationModel.activity_id.in_(activity_ids))

        return filters

    async def _get_activity_descendant_ids(self, title: str) -> list[int]:
        stmt = select(ActivityModel).where(ActivityModel.title.ilike(f'%{title}%'))
        result = await self._session.execute(stmt)
        root = result.scalar_one_or_none()
        if not root:
            return []

        ids = [root.id]

        stmt = select(ActivityModel)
        result = await self._session.execute(stmt)
        all_activities = result.scalars().all()

        def collect_descendants(parent_id: int):
            for a in all_activities:
                if a.parent_id == parent_id:
                    ids.append(a.id)
                    collect_descendants(a.id)

        collect_descendants(root.id)
        return ids

    async def get_organizations_by_filter(
            self,
            filter_params: FilterParamDTO | None,
            lat_min: float,
            lat_max: float,
            lon_min: float,
            lon_max: float,
    ) -> list[Organization]:
        filters = await self._build_organization_filters(filter_params)

        if None not in (lat_min, lat_max, lon_min, lon_max):
            filters.extend([
                BuildingModel.latitude.between(lat_min, lat_max),
                BuildingModel.longitude.between(lon_min, lon_max)
            ])

        query = (
            select(OrganizationModel)
            .join(OrganizationModel.building)
            .join(OrganizationModel.activity)
            .options(
                joinedload(OrganizationModel.building),
                joinedload(OrganizationModel.activity)
            )
            .filter(*filters)
        )

        result = await self._session.execute(query)
        models = result.scalars().all()
        return OrganizationMapper.models_to_entities(models)

    async def get_organization_by_id(self, organization_id: int) -> Organization | None:
        query = (
            select(OrganizationModel)
            .filter_by(id=organization_id)
            .options(joinedload(OrganizationModel.building), joinedload(OrganizationModel.activity)
            )
        )
        result = await self._session.execute(query)
        organization_model = result.scalar_one_or_none()
        return OrganizationMapper.model_to_entity(organization_model) if organization_model else organization_model

    async def get_organization_by_title(self, organization_title: str) -> Organization:
        query = (
            select(OrganizationModel)
            .filter_by(title=organization_title)
            .options(joinedload(OrganizationModel.building), joinedload(OrganizationModel.activity)
            )
        )
        result = await self._session.execute(query)
        organization_model = result.scalar_one_or_none()
        return OrganizationMapper.model_to_entity(organization_model) if organization_model else organization_model