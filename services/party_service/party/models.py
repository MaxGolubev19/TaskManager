from sqlalchemy.orm import Mapped

from services.party_service.database import Model, int_pk, created_at, updated_at


class PartyOrm(Model):
    __tablename__ = "party"

    id: Mapped[int_pk]
    name: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
