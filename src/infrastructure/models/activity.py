from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from organization import OrganizationModel


class ActivityModel(Base):
    __tablename__ = 'activities'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True)
    parent_id: Mapped[int | None] = mapped_column(ForeignKey('activities.id'), nullable=True)

    organizations: Mapped[list['OrganizationModel']] = relationship('OrganizationModel', back_populates='activity')