from sqlalchemy.orm import Mapped

from board_service.database import Model, int_pk, created_at, updated_at


class BoardOrm(Model):
    __tablename__ = "boards"

    id: Mapped[int_pk]
    name: Mapped[str]
    adventure_id: Mapped[int]
    party_id: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
