from sqlalchemy.orm import Mapped

from services.adventure_service.database import Model, int_pk, created_at, updated_at


class AdventureOrm(Model):
    __tablename__ = "adventure"

    id: Mapped[int_pk]
    name: Mapped[str]
    party_id: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
