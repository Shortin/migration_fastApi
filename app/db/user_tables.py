from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON

user_metadata = MetaData()


user_roles = Table(
    "user_roles",
    user_metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False)
)

users = Table(
    "users",
    user_metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(50), nullable=False),
    Column("username", String(100), nullable=False),
    Column("password", String(25), nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("user_role_id", Integer, ForeignKey("user_roles.id"))
)


