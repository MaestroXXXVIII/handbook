from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column

pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True, unique=True)]


class IntIdPkMixin:
    id: Mapped[pk]
