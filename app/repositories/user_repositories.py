from sqlalchemy import select

from app.db.database import new_session
from app.models.user_models import UsersTable, UserRolesTable
from app.schemas.user.user_schemas import SUserAdd, SUser
from app.schemas.user.user_role_schemas import SUserRoleAdd, SUserRole


class UsersRepository:
    @classmethod
    async def post_new_user(cls, data: SUserAdd) -> int:
        async with new_session() as session:
            new_user = UsersTable(**data.model_dump())
            session.add(new_user)
            await session.flush()
            await session.commit()
            return new_user.id

    @classmethod
    async def get_all_users(cls) -> list[SUser]:
        async with new_session() as session:
            query = select(UsersTable)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return [SUser.model_validate(user_model) for user_model in user_models]

    @classmethod
    async def get_user_by_id(cls, user_id: int) -> SUser:
        async with new_session() as session:
            query = select(UsersTable).where(UsersTable.id == user_id)
            result = await session.execute(query)
            return result.scalars().first()


class UserRolesRepository:
    @classmethod
    async def post_new_user_role(cls, data: SUserRoleAdd) -> int:
        async with new_session() as session:
            new_user_role = UserRolesTable(**data.model_dump())
            session.add(new_user_role)
            await session.flush()
            await session.commit()
            return new_user_role.id

    @classmethod
    async def get_all_user_roles(cls) -> list[SUserRole]:
        async with new_session() as session:
            query = select(UserRolesTable)
            result = await session.execute(query)
            user_role_models = result.scalars().all()
            return [SUserRole.model_validate(user_role_model) for user_role_model in user_role_models]

    @classmethod
    async def get_user_role_by_id(cls, user_role_id: int) -> SUserRole:
        async with new_session() as session:
            query = select(UserRolesTable).where(UserRolesTable.id == user_role_id)
            result = await session.execute(query)
            return result.scalars().first()
