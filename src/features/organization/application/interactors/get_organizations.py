from math import cos, radians

from src.features.organization.application.dtos import FilterParamDTO, OrganizationDTO
from src.features.organization.application.mapper import OrganizationMapper
from src.features.organization.domain.repository import IOrganizationRepository



class GetOrganizationsInteractor:
    def __init__(self, organization_repository: IOrganizationRepository):
        self._repository = organization_repository

    async def execute(self, query_params: FilterParamDTO | None) -> list[OrganizationDTO]:
        lat_min = lat_max = lon_min = lon_max = None

        if query_params and query_params.coordinates and query_params.radius:
            lat, lon = map(float, query_params.coordinates.split(','))
            lat_min, lat_max, lon_min, lon_max = self.get_bounding_box(lat, lon, query_params.radius)

        organizations = await self._repository.get_organizations_by_filter(
            filter_params=query_params,
            lat_min=lat_min,
            lat_max=lat_max,
            lon_min=lon_min,
            lon_max=lon_max
        )

        return [OrganizationMapper.entity_to_dto(o) for o in organizations]

    @staticmethod
    def get_bounding_box(lat: float, lon: float, radius_km: int) -> tuple[float, float, float, float]:
        """
        Вычисление диапазона координат попадающих в радиус
        """
        earth_radius = 6371
        delta_lat = radius_km / earth_radius * (180 / 3.1415926535)
        delta_lon = radius_km / (earth_radius * cos(radians(lat))) * (180 / 3.1415926535)

        return (
            lat - delta_lat,
            lat + delta_lat,
            lon - delta_lon,
            lon + delta_lon
        )
