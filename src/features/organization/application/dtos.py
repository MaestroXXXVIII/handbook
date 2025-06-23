from dataclasses import dataclass


@dataclass
class BuildingDTO:
    address: str
    coordinates: str


@dataclass
class ActivityDTO:
    activity_id: int
    title: str
    parent_id: int


@dataclass
class OrganizationDTO:
    organization_id: int
    title: str
    phone_number: str
    building: BuildingDTO
    activity: ActivityDTO


@dataclass
class FilterParamDTO:
    building_address: str | None
    activity_title: str | None
    coordinates: str | None
    radius: int | None
