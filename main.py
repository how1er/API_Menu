from fastapi import FastAPI
from app.routers import menus, submenus, dishes

import redis

from app import cache


app = FastAPI()


@app.on_event("startup")
async def startup():
    cache.cache = redis.from_url("redis://localhost")


@app.on_event("shutdown")
async def shutdown():
    await cache.cache.close()


app.include_router(menus.router, tags=["Menu"], prefix="/api/v1/menus")
app.include_router(
    submenus.router, tags=["SubMenu"], prefix="/api/v1/menus/{target_menu_id}/submenus"
)

app.include_router(
    dishes.router,
    tags=["Dish"],
    prefix="/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes",
)
