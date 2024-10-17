from sqlalchemy.orm import Mapped

from services.common.schemas.board_service.column_schemas import ColumnSpaceType
from services.board_service.database import Model, int_pk, created_at, updated_at


class ColumnOrm(Model):
    __tablename__ = "columns"

    id: Mapped[int_pk]
    space_id: Mapped[int]
    space_type: Mapped[ColumnSpaceType]
    order: Mapped[int]
    name: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
