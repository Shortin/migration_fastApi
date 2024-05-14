from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import new_session
from app.routes.user_router import users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Start, please wait")
    yield


title = "My base project FastAPI"
app = FastAPI(lifespan=lifespan, title=title, docs_url="/")
app.include_router(users_router)
