from fastapi import FastAPI
from  app.routers import menus, submenus, dishes


app = FastAPI()



app.include_router(menus.router, tags=['Menu'], prefix='/api/v1/menus')
app.include_router(submenus.router, tags=['SubMenu'], prefix='/api/v1/menus/{target_menu_id}/submenus')

app.include_router(dishes.router, tags=['Dish'], 
                    prefix='/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes')



