from typing import TYPE_CHECKING
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from organization import OrganizationModel


class BuildingModel(Base):
    __tablename__ = 'buildings'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    address: Mapped[str] = mapped_column(unique=True)
    latitude: Mapped[float] = mapped_column(nullable=False)
    longitude: Mapped[float] = mapped_column(nullable=False)

    organizations: Mapped[list['OrganizationModel']] = relationship('OrganizationModel', back_populates='building')
