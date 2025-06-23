from dataclasses import dataclass
import re

from src.features.organization.domain.entities.activity import Activity
from src.features.organization.domain.value_objects import Building


@dataclass
class Organization:
    organization_id: int
    title: str
    phone: str
    building: Building
    activity: Activity

    def __post_init__(self) -> None:
        self._validate_phone_number(self.phone)

    @staticmethod
    def _validate_phone_number(phone_number: str):
        if not phone_number.strip():
            raise ValueError(f'{phone_number} cannot be empty')

        pattern = r'^(\+7|8)\d{10}$'
        if not bool(re.match(pattern, phone_number)):
            raise ValueError(f'Incorrect phone number')
