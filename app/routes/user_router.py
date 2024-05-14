from typing import Annotated

from fastapi import APIRouter, Depends

from app.repositories.user_repositories import UsersRepository, UserRolesRepository
from app.schemas.answer_schema import SYesId
from app.schemas.user.user_role_schemas import SUserRoleAdd, SUserRole
from app.schemas.user.user_schemas import SUserAdd, SUser

users_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@users_router.post("/post_new_user")
async def post_new_user(
        user: Annotated[SUserAdd, Depends()],
):
    user_id = await UsersRepository.post_new_user(user)
    return {"user_id": user_id}


@users_router.get("/get_all_users")
async def get_all_users() -> list[SUser]:
    return await UsersRepository.get_all_users()


@users_router.get("/get_user/{user_id}", response_model=SUser)
async def get_user_by_id(user_id: int) -> SUser:
    return await UsersRepository.get_user_by_id(user_id)



@users_router.post("/post_new_user_role")
async def post_new_user_role(
        user_role: Annotated[SUserRoleAdd, Depends()],
):
    user_role_id = await UserRolesRepository.post_new_user_role(user_role)
    return {"user_role_id": user_role_id}


@users_router.get("/get_all_user_roles")
async def get_all_user_roles() -> list[SUserRole]:
    return await UserRolesRepository.get_all_user_roles()


@users_router.get("/get_user_role/{user_role_id}", response_model=SUserRole)
async def get_user_role_by_id(user_role_id: int) -> SUserRole:
    return await UserRolesRepository.get_user_role_by_id(user_role_id)
