import uuid

from sqlalchemy.orm import Mapped, mapped_column

from services.adventure_service.database import Model, created_at, updated_at


class AdventureOrm(Model):
    __tablename__ = "adventure"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    party_id: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
