from typing import Sequence

from src.features.organization.domain.entities.activity import Activity
from src.features.organization.domain.entities.organization import Organization
from src.features.organization.domain.value_objects import Building, Address, Coordinates
from src.infrastructure.models.organization import OrganizationModel


class OrganizationMapper:

    @staticmethod
    def models_to_entities(models: Sequence[OrganizationModel]) -> list[Organization]:
        entities = [
            Organization(
                organization_id=model.id,
                title=model.title,
                phone=model.phone,
                building=Building(
                    address=Address(model.building.address),
                    coordinates=Coordinates(f'{model.building.latitude}, {model.building.longitude}'),
                ),
                activity=Activity(
                    activity_id=model.activity.id,
                    title=model.activity.title,
                    parent_id=model.activity.parent_id,
                )
            )
            for model in models
        ]
        return entities

    @staticmethod
    def model_to_entity(model: OrganizationModel) -> Organization:
        return Organization(
                organization_id=model.id,
                title=model.title,
                phone=model.phone,
                building=Building(
                    address=Address(model.building.address),
                    coordinates=Coordinates(f'{model.building.latitude}, {model.building.longitude}'),
                ),
                activity=Activity(
                    activity_id=model.activity.id,
                    title=model.activity.title,
                    parent_id=model.activity.parent_id,
                )
            )