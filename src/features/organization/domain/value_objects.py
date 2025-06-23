from abc import ABC
from dataclasses import dataclass
import re


@dataclass(frozen=True)
class BaseValueObject(ABC):

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        pass


@dataclass(frozen=True)
class ValueObject[V](BaseValueObject, ABC):
    value: V

    def to_row(self) -> V:
        return self.value


@dataclass(frozen=True)
class Address(ValueObject[str]):

    def _validate(self) -> None:
        pattern = re.compile(
            r"^(г\.?\s*)?(?P<city>[\w\s\-]+),\s*(ул\.?\s*)?(?P<street>[\w\s\-]+)\s+(дом\s*)?(?P<building>\d+["
            r"а-яА-Яa-zA-Z\-/]*)(,\s*(?P<extra>.+))?$"
        )
        if not pattern.match(self.value):
            raise ValueError(f"Invalid address: {self.value}")


@dataclass(frozen=True)
class Coordinates(ValueObject[str]):

    def _validate(self):
        pattern = re.compile(r"^-?\d{1,3}\.\d+$")
        try:
            lat, lon = map(str.strip, self.value.split(","))
        except ValueError:
            raise ValueError(f"Invalid coordinates format: {self.value} (expected 'lat,lon')")

        if not pattern.match(lat) or not pattern.match(lon):
            raise ValueError(f"Invalid coordinates: {self.value}")


@dataclass(frozen=True)
class Building:
    address: Address
    coordinates: Coordinates
