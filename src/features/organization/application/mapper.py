from src.features.organization.application.dtos import OrganizationDTO, BuildingDTO, ActivityDTO
from src.features.organization.domain.entities.organization import Organization


class OrganizationMapper:

    @staticmethod
    def entity_to_dto(entity: Organization) -> OrganizationDTO:
        return OrganizationDTO(
            organization_id=entity.organization_id,
            title=entity.title,
            phone_number=entity.phone,
            building=BuildingDTO(address=entity.building.address.value, coordinates=entity.building.coordinates.value),
            activity=ActivityDTO(activity_id=entity.activity.activity_id, title=entity.activity.title, parent_id=entity.activity.parent_id),
        )
