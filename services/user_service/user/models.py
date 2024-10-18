from sqlalchemy.orm import Mapped

from services.user_service.database import Model, created_at, updated_at


class UserOrm(Model):
    __tablename__ = "user"

    name: Mapped[str]
    role_id: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
