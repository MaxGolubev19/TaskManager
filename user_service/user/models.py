from sqlalchemy.orm import Mapped, mapped_column

from user_service.database import Model, created_at, updated_at


class UserOrm(Model):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(primary_key=True)
    role_id: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
