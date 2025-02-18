from fastapi import Depends, FastAPI, APIRouter

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


# 定义路由器
router = APIRouter()


@router.get("/version")
async def get_items():
    return {"version": ["version1", "version2", "version3"]}


# 通过不同的前缀包含相同的路由器
app.include_router(router, prefix="/api/v1")
app.include_router(router, prefix="/api/latest")

# 定义第一个路由器
router_v1 = APIRouter()


@router_v1.get("/items1")
async def get_items_v1():
    return {"items": ["item1", "item2", "item3"]}


# 定义第二个路由器
router_v2 = APIRouter()


@router_v2.get("/items2")
async def get_items_v2():
    return {"items": ["itemA", "itemB", "itemC"]}


# 将 router_v2 包含到 router_v1 中
router_v1.include_router(router_v2, prefix="/v2")

# 包含 router_v1 到 FastAPI 应用中
app.include_router(router_v1, prefix="/api/v1")
