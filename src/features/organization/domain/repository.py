from abc import ABC, abstractmethod

from src.features.organization.application.dtos import FilterParamDTO
from src.features.organization.domain.entities.organization import Organization


class IOrganizationRepository(ABC):
    """
    Abstract class that represents the repository interface.
    """

    @abstractmethod
    async def get_organizations_by_filter(
            self,
            filter_params: FilterParamDTO,
            lat_min: float,
            lat_max: float,
            lon_min: float,
            lon_max: float,
    ) -> list[Organization]:
        """
        :param filter_params: parameters for filtering organizations
        :param lat_min: minimum latitude
        :param lat_max: maximum latitude
        :param lon_min: minimum longitude
        :param lon_max: maximum longitude
        :return: list of entities Organization
        """

    @abstractmethod
    async def get_organization_by_id(self, organization_id: int) -> Organization:
        """
        :param organization_id: organization id
        :return: entity Organization
        """

    @abstractmethod
    async def get_organization_by_title(self, organization_title: str) -> Organization:
        """
        :param organization_title: organization title
        :return: entity Organization
        """