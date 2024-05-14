from datetime import datetime

from sqlalchemy.orm import  Mapped, mapped_column, declarative_base

base = declarative_base()

class UsersTable(base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    username: Mapped[str]
    password: Mapped[str]
    registered_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    user_role_id: Mapped[int]


class UserRolesTable(base):
    __tablename__ = "user_roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

