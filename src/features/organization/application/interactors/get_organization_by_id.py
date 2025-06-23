from src.features.organization.application.dtos import OrganizationDTO
from src.features.organization.application.mapper import OrganizationMapper
from src.features.organization.domain.repository import IOrganizationRepository
from src.features.organization.exceptions import OrganizationNotFoundError


class GetOrganizationByIdInteractor:
    def __init__(self, organization_repository: IOrganizationRepository):
        self._repository = organization_repository

    async def execute(self, organization_id: int) -> OrganizationDTO:
        organization = await self._repository.get_organization_by_id(organization_id)

        if not organization:
            raise OrganizationNotFoundError(message=f'Organization with id={organization_id} not found')

        return OrganizationMapper.entity_to_dto(entity=organization)
